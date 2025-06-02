from services.users import get_user














@app.get("/users/user/", response_model = dict)
async def get_user(name):
    resp = get_user(name)
    
    return resp