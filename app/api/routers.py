from fastapi import APIRouter
from app.api.endpoints.users import users_router


routes = APIRouter()

routes.include_router(users_router, prefix="/users", tags=["users"])

# Additional routers or sub-routers can be included here

# Additional middleware or configuration specific to the v1 API can be added here
