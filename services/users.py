import psycopg2
from ..config.connect import connect

def update_user(name, surname, email, description, course, year, direction, CP, Password):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''UPDATE "user"."user"
	SET surname=%s, email=%s, description=%s, course=%s, year=%s, direction=%s, "CP"=%s, password=%s
	WHERE name=%s;''', (surname, email, description, course, year, direction, CP, Password, name))
        
        
        print("inserted correctly")
        return True
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)
        return False