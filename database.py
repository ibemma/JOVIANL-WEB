from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

# pip install python-dotenv
db_connection_string = os.getenv("DB_CONNECTION_STRING")


engine = create_engine(
    db_connection_string, connect_args={"ssl": {"ssl_ca": os.getenv("DB_CERT")}}
)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM bughiecareers.job;"))
        jobs = []
        for row in result.mappings().all():
            jobs.append(dict(row))
        return jobs
