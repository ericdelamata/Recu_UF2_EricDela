
from services.users import delete_user

 
@app.post("users/insert/", response_model=dict)
async def insertUser(name):
    correct = delete_user(name)
    
    return {"correcte":correct}