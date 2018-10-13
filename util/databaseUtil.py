import mysql.connector
import config
def connect():
    mydb = mysql.connector.connect(
    host=config.DATABASE_HOST,
    user=config.DATABASE_USER,
    passwd=config.DATABASE_PASSWORD,
    database=config.DATABASE_NAME
    )
    return mydb
def savedb(db,cursor):
    db.commit()
    cursor.close()
    db.close()
