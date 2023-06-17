from fastapi import APIRouter

from app.models.user import UserCreate, UserUpdate, UserInDB

router = APIRouter()


@router.post("/", response_model=UserInDB)
def create_user(user: UserCreate):
    # Logic to create a new user
    # Save user to the database and return the created user
    return user


@router.get("/{user_id}", response_model=UserInDB)
def get_user(user_id: int):
    # Logic to retrieve a user by ID
    # Query the database to get the user with the specified ID
    # Return the retrieved user
    return {"user_id": user_id, "username": "JohnDoe"}


@router.put("/{user_id}", response_model=UserInDB)
def update_user(user_id: int, user: UserUpdate):
    # Logic to update a user by ID
    # Query the database to get the user with the specified ID
    # Update the user with the new data provided in the request
    # Save the updated user to the database and return the updated user
    return {"user_id": user_id, "username": user.username, "email": user.email}


@router.delete("/{user_id}")
def delete_user(user_id: int):
    # Logic to delete a user by ID
    # Query the database to delete the user with the specified ID
    return {"message": f"User with ID {user_id} deleted successfully"}
