from pydantic import BaseModel
from ..enums.status_enum import StatusEnum

class HTTPResponseModel(BaseModel):
    status: StatusEnum
    data: dict