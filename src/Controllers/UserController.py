from models.User import createUser, getUserByUsername, updateUser, deleteUser

def create(request):
    data = request.get_json()
    createUser({
        "username": data["username"],
        "password": data["password"]
    })
    return {"message": "User created successfully"}

def get_user(request):
    username = request.args.get("username")
    user = getUserByUsername(username)
    if user:
        return user, 200
    else:
        return {"message": "User not found"}, 404

def update_user(request):
    data = request.get_json()
    username = data.get("username")
    update_data = data.get("update")
    updated_user = updateUser(username, update_data)
    if updated_user:
        return {"message": "User updated successfully"}, 200
    else:
        return {"message": "User not found"}, 404
    
def delete_user(request):
    username = request.args.get("username")
    deleted = deleteUser(username)
    if deleted:
        return {"message": "User deleted successfully"}, 200
    else:
        return {"message": "User not found"}, 404
