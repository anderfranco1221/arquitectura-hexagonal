import psycopg2
import os
from dotenv import load_dotenv
from app.infrastructure.exceptions import InvalidConectionDB

def conexion():
    load_dotenv()

    db_name = os.environ.get("DB_NAME", "test")
    db_user = os.environ.get("DB_USER", "admin")
    db_pass = os.environ.get("DB_PASS", "admin")
    db_host = os.environ.get("POSGRES_NAME", "localhost")
    db_port = os.environ.get("DB_PORT", "5432")

    try:  
        return psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_pass, port=db_port)
    except:
        raise InvalidConectionDB
       
    