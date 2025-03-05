from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    role = SelectField(
        "Role",
        choices=[("Batsman", "Batsman"), ("Bowler", "Bowler"), ("Wicket-Keeper", "Wicket-Keeper"), ("All-Rounder", "All-Rounder")],
        validators=[DataRequired()]
    )
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")
