import tables
from decouple import config
import connection as con

def create_db():
    cnx = con.get_cnx()
    cursor = cnx.cursor()
    cursor.execute("DROP DATABASE IF EXISTS {}".format(config('DB_NAME')))
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(config('DB_NAME')))
    print("Database Creation Successful")

def create_tables():
    cnx = con.get_db()
    cursor = cnx.cursor()
    print("Table Creation Initiated")
    for table in tables.TABLES:
        cursor.execute(table)
    print("Table Creation Successful")

if __name__ == "__main__":
    create_db()
    create_tables()
