from flask import render_template, abort, redirect, url_for, request, flash
from flask_login import current_user, login_required
from . import main
from ..requests import random
from ..models import User, Blogs
from .forms import UpdateProfile, BlogsForm
from .. import db, photos

@main.route('/')
def index():
    
    random_quote = random()
    blogs = Blogs.query.all()

    return render_template('index.html', random = random_quote, blogs = blogs, blogger = blogs)
    
@main.route('/user/<uname>') 
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blogs.get_blog(user.id)
    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user, blogs = blogs ) 

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form) 
    
@main.route('/user/<uname>/update/pic', methods=['POST']) 
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first() 
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=uname))     

@main.route('/user/blog/new', methods =['GET', 'POST'])
@login_required
def new_blog():
    form = BlogsForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_pitch = Blogs(title = title, content = content, blogger = current_user)
        new_pitch.save_blog()
        flash('Pitch posted')
        return redirect(url_for('.profile', uname = current_user.username ))

    return render_template('new_blog.html', blog_form = form)
