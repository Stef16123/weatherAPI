from fastapi import APIRouter

router = APIRouter(
    prefix="/weather",
    tags=["weather"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/")
async def weather():
    return {"message":"WIP"}

