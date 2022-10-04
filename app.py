import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '20B1FAC1B79B6BA380AB8297C6E0F4B6'

db = SQLAlchemy(app)
bootstrap = Bootstrap5(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return '<h1>Login is being performed</h1>'
    else:
        return '<h1>Here you can see a login form</h1>'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'<h1>{username}\'s profile</h1>'

@app.route('/greeting/')
@app.route('/greeting/<name>')
def greeting(name=None):
    temperatures = [10, 15, 20, 25, 30]

    greeting_msgs = {
        'morning': 'Good morning!',
        'day': 'Good afternoon!',
        'evening': 'Good evening!',
        'night': 'Good night!',
        }

    funny_msgs = [
        'I like it.',
        'I dislike it.',
        ]

    params = {
        'name': 'name',
        'temperatures': 'temperatures',
        'greeting_msgs': 'greeting_msgs',
        'funny_msgs': 'funny_msgs',
    }

    return render_template(
        'greeting.html',
        # **params,
        name=name,
        temperatures=temperatures,
        greeting_msgs=greeting_msgs,
        funny_msgs=funny_msgs
    )