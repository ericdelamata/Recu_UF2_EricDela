import psycopg2
from ..config.connect import connect

def insert_user(name, surname, email, description, course, year, direction, CP, Password):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO "user"."user"(
	    name, surname, email, description, course, year, direction, "CP", password)
	    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (name, surname, email, description, course, year, direction, CP, Password))
        
        
        print("inserted correctly")
        return True
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)
        return False