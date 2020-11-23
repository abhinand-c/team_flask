from database import connection as con

def _insert(table, data):
    statement = "INSERT INTO " + table + " "
    fields=""
    value_placeholder=""
    values=()
    for (key,val) in data.items():
        fields+=key + ", "
        value_placeholder+= "%s, "
        values+=(val,)
    statement += "(" + fields[:-2] + ") VALUES (" + value_placeholder[:-2] + ") "
    return statement, values

def get_data(table):
    cnx = con.get_db()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM " + table)
    return cursor.fetchall()

def add_data(table, data):
    cnx = con.get_db()
    cursor = cnx.cursor()
    statement, values = _insert(table, data)
    cursor.execute(statement, values)
    cnx.commit()
    print("Data Successfully inserted")
