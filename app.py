from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": "1",
        "title": "Data Analyst",
        "location": "Lekki, Lagos",
        "salary": "NGN. 120,000",
    },
    {
        "id": "2",
        "title": "Fontend Engineer",
        "location": "Missouri, USA ",
        "salary": "$45,000",
    },
    {
        "id": "3",
        "title": "Office Assistance",
        "location": "portharcourt, Nigeria",
    },
    {
        "id": "4",
        "title": "Financial Secretary",
        "location": "Paris, France",
        "salary": "EUR. 50,000",
    },
]


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == ("__main__"):
    app.run(host="0.0.0.0", debug=True)
