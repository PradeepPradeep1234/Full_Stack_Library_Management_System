from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=25)], render_kw={"placeholder": "Enter your username"})
    password = PasswordField("Password", validators=[DataRequired()],render_kw={"placeholder": "Enter your Password"})
    role = SelectField("Role", choices=[("user", "User"), ("admin", "Admin")], default="user")
    submit = SubmitField("Register")
