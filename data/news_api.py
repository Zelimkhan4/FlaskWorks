from flask import Blueprint, jsonify, make_response, request, abort
from . import db_session
from .jobs import Jobs



# Задачи 1, 2, 4, 5

bp = Blueprint(
    "jobs_api",
    __name__,
    template_folder="templates"
)

@bp.route("/api/jobs", methods=["GET"])
def get_jobs():
    sess = db_session.create_session()
    works = sess.query(Jobs).all()
    res = {"jobs": [work.to_dict(columns=["id", "team_leader", "job", "collaborators", "work_size",
                                          "position", "start_data", "end_date", "is_finished"]) for work in works]}
    return jsonify(res)


@bp.route("/api/jobs/<int:job_id>")
def get_one_job(job_id):
    sess = db_session.create_session()
    job = sess.query(Jobs).get(job_id)
    print(request.__dict__)
    if job:
        res = jsonify(job=job.to_dict(columns=["id", "job"]))
        return make_response(res, 200)
    return make_response(jsonify(error="not found"), 404)


@bp.route("/api/jobs", methods=["POST"])
def add_jobs():
    if request.json and all([i in request.json.keys() for i in ["id", "job", "team_leader"]]):

        sess = db_session.create_session()
        job = sess.query(Jobs).get(request.json["id"])

        if job:
            return make_response(jsonify(error="Id already exists"), 400)
        job = Jobs()

        for attr in request.json.keys():
           job.__setattr__(attr, request.json[attr])
        sess.add(job)
        sess.commit()

        return make_response(jsonify(f"Job #{job.id} is added."), 200)
    return make_response(jsonify(error="Bad request"), 400)
