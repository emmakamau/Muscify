from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired


class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Album review')
    submit = SubmitField('Submit')
