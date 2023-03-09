from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class AddJobsForm(FlaskForm):
    team_leader = IntegerField("Teamleader", validators=[DataRequired()])
    job = StringField("Job", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    work_size = IntegerField("Work size", validators=[DataRequired()])
    is_finished = BooleanField("Is finished")
    submit = SubmitField("Добавить работу")

