from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField , SelectField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us something about yourself", validators=[DataRequired()])
    submit = SubmitField('Submit')

class BlogsForm(FlaskForm):

    title = StringField('Pitch title', validators=[DataRequired()])
    content = CKEditorField('Write your pitch', validators=[DataRequired()] )
    submit = SubmitField('Submit') 