#Jeremy Krovitz

#File creates the ReviewForm class, which defines the fields that are used in the
#form.
#-----------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

class ReviewForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(min=1)])
    text = TextAreaField('Review', validators=[DataRequired(), Length(min=1)])
    rating = IntegerField('Rate movie between 1 and 5', validators=[NumberRange(min=1, max=5)])
    submit = SubmitField('Submit')
