from fastapi import APIRouter


sub_app_router = APIRouter(prefix="/subApp", tags=["subApp"])


@sub_app_router.post("/whoami")
async def whoami():
    raise ValueError("i don't know")
