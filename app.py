from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from flaskr import registration, authentication

app = Flask(__name__)

app.config.from_object(config.DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/', methods=["GET", "POST"])
@app.route('/registration', methods=["GET", "POST"])
def register_page():
    return registration.start()


@app.route("/auth", methods=["GET", "POST"])
def auth():
    return authentication.start()


@app.route("/laboratory")
def lab():
    return render_template('laboratory.html')


if __name__ == '__main__':
    app.run()
