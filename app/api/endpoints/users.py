from fastapi import APIRouter, Depends
from app.core.database import get_db

from app.models.users import User, UserCreate, UserResponse
from sqlalchemy.orm import Session


users_router = APIRouter()


@users_router.get("/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [UserResponse.from_orm(user) for user in users]


@users_router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.id == user_id).all()
    return [UserResponse.from_orm(user) for user in users]


@users_router.post("/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        name=user.name,
        surname=user.surname,
        email=user.email,
        password_hash=user.password_hash,
        last_login=user.last_login,
        xp_points=user.xp_points,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse.from_orm(db_user)


@users_router.put("/{user_id}")
async def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    for key, value in user_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return UserResponse.from_orm(user)


@users_router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return {"message": f"User #{user_id} deleted"}
