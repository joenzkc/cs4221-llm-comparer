import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import pool

load_dotenv()
DB_URL = os.environ.get('DB_URL')
db_pool = pool.SimpleConnectionPool(1, 10, DB_URL)

def get_connection():
    return db_pool.getconn()

def close_connection(connection):
    db_pool.putconn(connection)

def get(sql):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except psycopg2.Error as e:
        result = 'Error: ' + str(e)
    finally:
        cursor.close()
        close_connection(connection)
    return result

def insert(sql):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        close_connection(connection)