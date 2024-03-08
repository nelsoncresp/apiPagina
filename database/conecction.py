# conectar a la base de datos
import pymysql.cursors

def get_db_connection():
    connection = pymysql.connect(
        host='localhost:3306',
        user='root',
        password='',
        db='pag_vuelos',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
