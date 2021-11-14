from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[DataRequired()])
    post = TextAreaField("Type Away:", validators=[DataRequired()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[DataRequired()])
    post = TextAreaField("Type Away", validators=[DataRequired()])
    submit = SubmitField("Update")

