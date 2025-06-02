def user_schema(user) -> dict:
    resp = {
        "name":user[0],
        "surname":user[1],
        "email":user[2],
        "description":user[3],
        "course":user[4],
        "year":user[5],
    }
    
    return resp

def users_schema(users) -> list[dict]:
    
    response = [user_schema(user) for user in users]
    
    return response