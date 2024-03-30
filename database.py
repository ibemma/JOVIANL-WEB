from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

# pip install python-dotenv
db_connection_string = os.getenv("DB_CONNECTION_STRING")


engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {"ssl_ca": os.getenv("DB_CERT")}},
    pool_timeout=7,
    pool_recycle=60,
    pool_pre_ping=True,
    isolation_level="AUTOCOMMIT",
)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM bughiecareers.job;"))
        jobs = []
        for row in result.mappings().all():
            jobs.append(dict(row))
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        val = id
        result = conn.execute(text(f"select * from bughiecareers.job where id = {val}"))
        rows = result.mappings().all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])


def add_application_to_db(
    job_id, full_name, email, linkedin_url, education, work_experience, resume_url
):

    with engine.connect as conn:

        query = text(
            "INSERT INTO `bughiecareers`.`application` (`job_id`, `full_name`, `email`, `linkedin_url`, `education`, `work_experience`, `resume_url`)  VALUES("
            + job_id
            + full_name
            + email
            + linkedin_url
            + education
            + work_experience
            + resume_url
            + ");"
        )
        conn.execute(query)
        conn.commit()
