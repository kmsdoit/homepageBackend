from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def DBConnection() :
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_DATABASE = os.environ.get('DB_DATABASE')
    database = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}")
    conn = database.connect()
    return conn