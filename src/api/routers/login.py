from fastapi import APIRouter, Request, Response

from src.models.dtos.login import LoginDTO
from src.core import login


router = APIRouter(prefix="/api/login")


@router.post('')
def get(dto: LoginDTO, req: Request, res: Response):

    return login.create(dto)
