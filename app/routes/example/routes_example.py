from fastapi import APIRouter
from ..models.model_http_response import HTTPResponseModel
from ..enums.enum_status import StatusEnum

router = APIRouter(
    prefix="/example"
)

@router.get("/test")
async def example():
    return HTTPResponseModel(
        status=StatusEnum.SUCCESS,
        data={
            "message": "this was a successful test"
        }
    )