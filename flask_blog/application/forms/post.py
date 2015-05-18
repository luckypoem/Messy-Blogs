# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(Form):
    title = StringField('标题', validators=[DataRequired()])
    content = TextAreaField('内容', validators=[DataRequired()])
