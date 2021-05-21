from wtforms import *


class AuthenticationForm(Form):
    login = TextField('login', [validators.Length(min=4, max=20)])
    api = TextField('api', [validators.Length(min=6, max=50)])
