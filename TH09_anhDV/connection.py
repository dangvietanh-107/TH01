import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test1"
        )
        return conn
    except mysql.connector.Error as e:
        print("Lỗi kết nối cơ sở dữ liệu:", e)
        return None
