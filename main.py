from data import db_session
from flask import Flask, render_template, redirect
from flask_login import LoginManager, logout_user
from data.jobs import Jobs
from data.users import User
from forms.login_form import LoginForm
from flask_login import login_user, login_required, current_user
from forms.add_jobs import AddJobsForm
from forms.register import RegisterForm


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


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


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

@login_required
@app.route("/add_job", methods=["POST", "GET"])
def add_job():
    form = AddJobsForm()
    if form.validate_on_submit():
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            collaborators=form.collaborators.data,
            work_size=form.work_size.data,
            is_finished=form.is_finished.data
        )
        job.user = current_user
        sess = db_session.create_session()
        sess.merge(job)
        sess.commit()
        return redirect("/")
    return render_template("add_jobs.html", form=form)


@app.route("/register", methods=["POST", 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        sess = db_session.create_session()
        if sess.query(User).filter(User.email == form.email.data).first():
            return render_template("register.html", form=form, message="Пользователь с таким email уже существует.")
        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.address = form.address.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.age = form.age.data
        user.email = form.email.data
        user.set_password(form.password.data)
        sess.add(user)
        sess.commit()
        return redirect("/login")
    return render_template("register.html", form=form)


if __name__ == "__main__":
    db_session.global_init("db/blog.db")
    # sess = db_session.create_session()
    # user = sess.query(User).filter(User.email == "DartZelamh@mail.ru").first()
    # user.name = "Zelimkhan"
    # sess.add(user)
    # sess.commit()
    app.run()