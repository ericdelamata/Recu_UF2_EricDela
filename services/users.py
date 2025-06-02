import psycopg2
from ..config.connect import connect

def update_user(name, surname, email, description, course, year, direction, CP, Password):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('''UPDATE "user"."user"
	SET surname=%s, email=%s, description=%s, course=%s, year=%s, direction=%s, "CP"=%s, password=%s
	WHERE name=%s;''', (surname, email, description, course, year, direction, CP, Password, name))
        
        return True
    except(Exception, psycopg2.Error) as error:
        print("Error: ", error)
        return False

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
