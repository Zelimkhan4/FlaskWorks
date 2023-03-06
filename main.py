from data import db_session
from flask import Flask, render_template
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)


@app.route("/works")
def works():
    sess = db_session.create_session()
    works = sess.query(Jobs).all()
    return render_template("works.html", works=works)


if __name__ == "__main__":
    db_session.global_init("db/blog.db")
    app.run()