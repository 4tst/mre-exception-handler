from fastapi import APIRouter


user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post("/whoami")
async def whoami():
    raise ValueError("i don't know")
