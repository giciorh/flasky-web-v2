from sqlalchemy import create_engine, text
import os

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine =  create_engine(
  db_conn_string,
  connect_args={
    "ssl": {
        "ca": "/etc/ssl/certs/ca-certificates.crt",
    }
}
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = []
  
    for row in result.all():
      jobs.append(row._mapping)
      #jobs.append(dict(row._mapping))
  return jobs

#get specify job by given id  
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id=:val_id")
      .bindparams(val_id=id)
    )
  rows = result.all()
  if len(rows) == 0:
    return None
  else:
    return dict(rows[0]._mapping)