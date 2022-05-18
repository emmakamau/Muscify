from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import InputRequired
   
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])


class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[InputRequired()])
    review = TextAreaField('Album review')
    submit = SubmitField('Submit')
