from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell people about yourself.',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Elevator pitch','Elevator pitch'),('Interview pitch','Interview pitch'),('Pickup line','Pickup line'),('Pun','Pun')],validators=[InputRequired()])
    text = TextAreaField('Pitch', validators=[InputRequired()])
    submit = SubmitField('Save')  

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment') 