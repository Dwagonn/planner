from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class MealForm(FlaskForm):
    name = StringField('Meal Name', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients (comma-separated)', validators=[DataRequired()])
    submit = SubmitField('Add Meal')

class PlanForm(FlaskForm):
    # Will dynamically set choices in view
    day = StringField('Day')
    meal = SelectField('Meal', coerce=int)
    submit = SubmitField('Save Plan')
