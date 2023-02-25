from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Wrocław',
  'salary': '10 000 zł'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Kraków',
  'salary': '13 000 zł'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Gdańsk',
  'salary': '9 000 zł'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Katowice',
}, {
  'id': 5,
  'title': 'Junior Python Dev',
  'location': 'Poznań',
  'salary': '6 000 zł'
}]


#dodano make api
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route("/")
def hello_world():
  return render_template("hello.html", jobs=JOBS, company_name='Flasky')


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
