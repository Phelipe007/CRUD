import mysql.connector

def db_connection():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="181299",
        database="bdyoutube"
    )
    return conexao

