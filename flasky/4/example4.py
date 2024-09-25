from flask import Flask, render_template
from flask import session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
# from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pxli'
bootstrap = Bootstrap(app)
moment = Moment(app)

# def uoft_email(form, field):
#     if 'utoronto' not in field.data:
#         raise ValidationError('Please use your UofT email address.')
    
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    # email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email(), uoft_email])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    is_uoft_email=True
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
            
        if 'utoronto' in form.email.data:
            is_uoft_email=True
        else:
            is_uoft_email=False
        
        session['name'] = form.name.data
        session['email']=form.email.data
        session['is_uoft_email']=is_uoft_email
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),email=session.get('email'),is_uoft_email=session.get('is_uoft_email'))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name='Peixuan')

