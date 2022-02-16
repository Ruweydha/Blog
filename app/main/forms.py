from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField , SelectField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us something about yourself", validators=[DataRequired()])
    submit = SubmitField('Submit')

class BlogsForm(FlaskForm):

    title = StringField('Blog title', validators=[DataRequired()])
    content = CKEditorField('Write your Blog', validators=[DataRequired()] )
    submit = SubmitField('Submit') 

class CommentsForm(FlaskForm):
    
    comment = CKEditorField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SubscriptionForm(FlaskForm):
    email = email = StringField('Subscribe to be alerted when a new blog is posted', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')