from sqlalchemy import create_engine
from dotenv import load_dotenv
from models import *
import os

load_dotenv()

user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
db = os.getenv("db")

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, db)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base.metadata.create_all(bind=engine)
