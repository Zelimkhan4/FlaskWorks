from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Jobs(FlaskForm):
    team_leader = IntegerField("Teamleader", validators=[DataRequired()])
    job = StringField("Job", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    work_size = IntegerField("Work size", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    start_data = DateTimeField("Start data", validators=[DataRequired()])
    end_date = DateTimeField("End date", validators=[DataRequired()])
    is_finished = BooleanField("Is finished", validators=[DataRequired()])
    submit = SubmitField("Добавить работу")

