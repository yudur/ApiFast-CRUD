import mysql.connector

from dotenv import load_dotenv
import os

load_dotenv()

def create_database():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password=os.getenv("PASSWORD_MYSQL"),
            host='127.0.0.1'
        )

        mycursor = cnx.cursor()
        mycursor.execute("CREATE DATABASE crudfastapi")
        cnx.close()
        mycursor.close()
    except Exception as err:
        print("Something went wrong ->", err)
        return
    
    try:
        db = mysql.connector.connect(
            user='root',
            password=os.getenv("PASSWORD_MYSQL"),
            host='127.0.0.1',
            database='crudfastapi'
        )

        command = "CREATE TABLE users(\nid INT(1) NOT NULL AUTO_INCREMENT,\nnome VARCHAR(155) NOT NULL,\nemail VARCHAR(255),\ntelefone VARCHAR(11),\nPRIMARY KEY (id)\n);"
        cursor = db.cursor()
        cursor.execute(command)
        db.commit()
        print("database created successfully")
    except Exception as err:
        print("Something went wrong ->", err)
        return
    
create_database()
