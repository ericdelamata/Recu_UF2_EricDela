
from services.users import update_user


@app.post("users/update/", response_model=dict)
async def updateUser(name, surname, email, description, course, year, direction, CP, Password):
    correct = update_user(name, surname, email, description, course, year, direction, CP, Password)
    
    return {"correcte":correct}