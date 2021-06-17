from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, TextField, validators
from binance import Client

import config
import models


class RegistrationForm(Form):
    login = TextField('login', [validators.Length(min=4, max=20)])
    api = TextField('api', [validators.Length(min=6, max=50)])
    secret = TextField('secret', [validators.Length(min=6, max=50)])


def start():
    app = Flask(__name__)

    app.config.from_object(config.DevelopmentConfig)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    try:
        form = RegistrationForm(request.form)

        if request.method == 'POST':
            login = form.login.data
            api = form.api.data
            secret = form.secret.data

            if models.User.query.filter_by(login=login).first() is None:
                client = Client(api, secret)
                client.get_account_snapshot(type='SPOT')
                db.session.add(models.User(login, api, secret))
                db.session.commit()
                flash('You registered successfully!')
                return render_template('laboratory.html', form=form)
            else:
                flash('That username is already taken, please choose another')
                return render_template('registration.html', form=form)

    except Exception as e:
        print(e.__traceback__)
        flash('Invalid API or Secret Key!')
        return render_template('registration.html', form=form)

    return render_template('registration.html', form=form)
