from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, TextField, validators

import config
import models


class AuthenticationForm(Form):
    login = TextField('login', [validators.Length(min=4, max=20)])
    api = TextField('api', [validators.Length(min=6, max=50)])


def start():
    app = Flask(__name__)

    app.config.from_object(config.DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    try:
        form = AuthenticationForm(request.form)

        if request.method == 'POST':
            login = form.login.data
            api = form.api.data
            user = models.User.query.get(login)

            if api == user.api_key:
                flash('You logged in successfully!')
                return render_template('laboratory.html', form=form)
            else:
                flash('Invalid data')
                return render_template('auth.html', form=form)

    except Exception as e:
        flash('Invalid data')
        return str(e)

    return render_template('auth.html', form=form)
