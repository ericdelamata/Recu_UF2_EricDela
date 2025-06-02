import psycopg2
from ..config.connect import connect

















def get_user(name):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''SELECT name, surname, email, description, course, year FROM "user"."user" WHERE name=%s;''', (name))
        
        user = cursor.fetchone()
        
        return user
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)
        return {"Error": error}