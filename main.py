from Services.users import insert_user

@app.post("users/insert/", response_model=dict)
async def insertUser(name, surname, email, description, course, year, direction, CP, Password):
    correct = insert_user(name, surname, email, description, course, year, direction, CP, Password)
    
    return {"correcte":correct}