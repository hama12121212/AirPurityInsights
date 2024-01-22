import os

DB_NAME = os.getenv("DB_NAME", "aqe")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

SQLALCHEMY_DATABASE_URI = (
    "postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}".format(
        db_name=DB_NAME,
        db_user=DB_USER,
        db_pass=DB_PASS,
        db_host=DB_HOST,
        db_port=DB_PORT,
    )
)
