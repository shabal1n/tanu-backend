from fastapi import APIRouter

from app.api.endpoints import users

routes = APIRouter()

routes.include_router(users.router, prefix="/users", tags=["users"])

# Additional routers or sub-routers can be included here

# Additional middleware or configuration specific to the v1 API can be added here
