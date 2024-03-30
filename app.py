from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db


app = Flask(__name__)

jobs = load_jobs_from_db()


@app.route("/")
def hello_bughie():
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404

    return render_template("jobPage.html", job=job)


@app.route("/job/<id>/apply", methods=["GET", "POST"])
def apply_to_job(id):
    job = load_job_from_db(id)
    if request.method == "post":
        # job_id = id
        # full_name = request.form.get("full_name", False)
        # email = request.form.get("email", False)
        # linkedin_url = request.form.get("linkedin_url", False)
        # education = request.form.get("education", False)
        # work_experience = request.form.get("work_experience", False)
        # resume_url = request.form.get("resume_url", False)

        job_id = id
        full_name = request.form["full_name"]
        email = request.form["email"]
        linkedin_url = request.form["linkedin_url"]
        education = request.form["education"]
        work_experience = request.form["work_experience"]
        resume_url = request.form["resume_url"]

        # store this in the DB
        # send an email
        # add_application_to_db(
        #     job_id,
        #     full_name,
        #     email,
        #     linkedin_url,
        #     education,
        #     work_experience,
        #     resume_url,
        # )

    else:
        return render_template("appli_submit.html", data=request.form, job=job)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
