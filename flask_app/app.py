from flask import Flask, request, render_template
from forms import SignupForm

from flask_app import db, create_app
from models import User
from flask_login import LoginManager, login_user, login_required, logout_user

app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(email):
    return User.query.filter_by(email=email).first()


@app.route('/')
def index():
    return "Welcome to Flask"


def create_user(email_data, password_data):
    newuser = User(email_data, password_data)
    print(newuser.password)
    db.session.add(newuser)
    db.session.commit()
    return newuser


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).first():
                return "Email address already exists"
            else:
                new_user = create_user(form.email.data, form.password.data)
                login_user(new_user)
                return "User Created!"
        else:
            return "Form did not validate"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignupForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                if user.check_password(form.password.data):
                    login_user(user)
                    return "User logged in"
                else:
                    return "Wrong password"
            else:
                return "User does not exist"
        else:
            return "form not validated"


@app.route('/protected')
@login_required
def protected():
    return "protected area"


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"


if __name__ == '__main__':
    # app.init_db()
    app.run(port=8000, host='localhost')
