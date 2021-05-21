from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
import models
from flaskr import registration, authentication

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/', methods=["GET", "POST"])
@app.route('/registration', methods=["GET", "POST"])
def register_page():
    try:
        form = registration.RegistrationForm(request.form)

        if request.method == 'POST':
            login = form.login.data
            api = form.api.data
            secret = form.secret.data

            if models.User.query.filter_by(login=login).first() == 'None':
                db.session.add(models.User(login, api, secret))
                db.session.commit()
                flash('You registered successfully!')
                return render_template('registration.html', form=form)
            else:
                flash('That username is already taken, please choose another')
                return render_template('registration.html', form=form)

    except Exception as e:
        print(e)
        return str(e)

    return render_template('registration.html', form=form)


@app.route("/auth", methods=["GET", "POST"])
def auth():
    try:
        form = authentication.AuthenticationForm(request.form)

        if request.method == 'POST':
            login = form.login.data
            api = form.api.data

            if models.User.query.filter_by(login=login, api_key=api).first().login == login:
                print(models.User.query.filter_by().all())
                flash('You registered successfully!')
                db.session['logged_in'] = True
                db.session['login'] = login
                return render_template('auth.html', form=form)
            else:
                for model in models.User.query.filter_by().all():
                    print(model)
                flash('That username is already taken, please choose another')
                return render_template('auth.html', form=form)

    except Exception as e:
        print(e)
        return str(e)

    return render_template('auth.html', form=form)


@app.route("/details")
def get_book_details():
    author = request.args.get('author')
    published = request.args.get('published')
    return "Author : {}, Published: {}".format(author, published)


if __name__ == '__main__':
    app.run()
