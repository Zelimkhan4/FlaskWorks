from data import db_session
from flask import Flask, render_template, redirect
from flask_login import LoginManager
from data.jobs import Jobs
from data.users import User
from forms.login_form import LoginForm
from flask_login import login_user, login_required


app = Flask(__name__)
app.config["SECRET_KEY"] = "gdsfotyerer"


login_manager = LoginManager()
login_manager.init_app(app)





@login_manager.user_loader
def load_user(user_id):
    sess = db_session.create_session()
    return sess.query(User).filter(User.id == user_id).first()



@app.route("/")
def works():
    sess = db_session.create_session()
    works = sess.query(Jobs).all()
    return render_template("works.html", works=works)


@app.route("/login", methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        sess = db_session.create_session()
        user = sess.query(User).filter(User.email == login_form.email.data).first()
        if user and user.check_password(login_form.password.data):
            login_user(user)
            return redirect("/")
        return render_template("login.html", form=login_form, message="Неправильная почта или пароль!")
    return render_template("login.html", form=login_form)



if __name__ == "__main__":
    db_session.global_init("db/blog.db")
    app.run()
