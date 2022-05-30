from typing import List
from fastapi import APIRouter, HTTPException, Request, Response, UploadFile

from src.core import files
from src.models.dtos.file import FileDTO
from src.models.dtos.user import SimpleUserDTO


router = APIRouter(prefix='/api/files')


@router.get('/{user}')
def get_all(user:str, req: Request, res: Response):
    
    return files.get_all(user, req)


@router.get('/download')
def get(user:str, dto: FileDTO, req: Request, res: Response):
    
    return files.get(dto)


@router.post('/{user}')
async def post(user:str, req: Request, file: List[UploadFile]):
    
    return await files.create(user, req, file)


@router.delete('')
def delete(dto: FileDTO, req: Request, res: Response):
    
    return files.delete(dto)
