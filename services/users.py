import psycopg2
from ..config.connect import connect

def delete_user(name):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''DELETE FROM "user"."user"
	WHERE name=%s;''', (name))
        
        
        print("deleted correctly")
        return True
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)
        return False