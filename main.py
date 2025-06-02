

from services.users import get_user, insert_user, update_user


@app.post("users/update/", response_model=dict)
async def updateUser(name, surname, email, description, course, year, direction, CP, Password):
    correct = update_user(name, surname, email, description, course, year, direction, CP, Password)
    
    return {"correcte":correct}

@app.get("/users/user/", response_model = dict)
async def get_user(name):
    resp = get_user(name)
    
    return resp
 
@app.post("users/insert/", response_model=dict)
async def insertUser(name, surname, email, description, course, year, direction, CP, Password):
    correct = insert_user(name, surname, email, description, course, year, direction, CP, Password)
    
    return {"correcte":correct}
