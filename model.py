import psycopg2
from psycopg2 import sql

def connect():
    try:
        conn = psycopg2.connect(
            database="dbtest", 
            user="postgres",    
            password="yourpassword",  
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

def select_data():
    conn = connect()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM sinhvien;")
        rows = cur.fetchall()
        conn.close()
        return rows
    return []
