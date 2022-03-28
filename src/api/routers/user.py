from fastapi import APIRouter, Request, Response
from pydantic import UUID4

from src.models.dtos.user import UserDTO
from src.core import user


router = APIRouter(prefix="/api/user")


@router.get('')
def get(req: Request, res: Response):

    return user.get_all()


@router.post('')
def get(dto: UserDTO, req: Request, res: Response):

    return user.create(dto)


@router.delete('/{id}')
def get(id: UUID4, req: Request, res: Response):

    return user.delete(id)
