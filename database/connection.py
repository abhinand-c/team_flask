from decouple import config
import mysql.connector

access = {
    "user": config("DB_USER"),
    "password": config("DB_PASSWORD"),
    "host": config('DB_HOST')
}

access_db = {**access, "database": config('DB_NAME')}

def get_cnx():
    print(" -- Establishing DB connection (No database Selected)-- ")
    return mysql.connector.connect(**access)

def get_db():
    print(" -- Establishing DB connection -- ")
    return mysql.connector.connect(**access_db)
