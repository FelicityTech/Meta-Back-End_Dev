# Ensure compliance with data protection regulation 
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        # Store the user's data securely
        # ...
        return redirect(url_for('signup.html', form=form))
    