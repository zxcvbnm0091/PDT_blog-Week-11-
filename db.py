import psycopg2

def db_connection():
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='test',
        user='postgres',
        password='admin'
    )
    return conn
