from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

# JOBS = [{
#   'id': 1,
#   'title': 'Data Analyst',
#   'location': 'Wrocław',
#   'salary': '10 000 zł'
# }, {
#   'id': 2,
#   'title': 'Data Scientist',
#   'location': 'Kraków',
#   'salary': '13 000 zł'
# }]


#dodano make api
@app.route("/api/jobs")
def list_jobs():
  return jsonify(load_jobs_from_db())
  #return jsonify(JOBS)


@app.route("/")
def hello_world():
  JOBS = load_jobs_from_db()
  return render_template("hello.html", jobs=JOBS)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)

  if not job:
    return "<h3>Not found</h3>", 404

  return render_template('jobpage.html', job=job)


# @app.route("/job/<id>")
# def show_job(id):
#   job = load_job_from_db(id)
#   return jsonify(job)


@app.route("/about")
def hello_about():
  return hello_world()


@app.route("/events")
def hello_events():
  return hello_world()


@app.route("/learn")
def hello_learn():
  return hello_world()


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)

  add_application_to_db(id, data)
  return render_template("application_submitted.html",
                         application=data,
                         job=job)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
