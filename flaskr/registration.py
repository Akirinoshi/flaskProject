from wtforms import *


class RegistrationForm(Form):
    login = TextField('login', [validators.Length(min=4, max=20)])
    api = TextField('api', [validators.Length(min=6, max=50)])
    secret = TextField('secret', [validators.Length(min=6, max=50)])


def register():
    try:
        form = RegistrationForm(request.form)

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
