from typing import List
from fastapi import APIRouter, HTTPException, Request, Response, UploadFile

from src.core import files
from src.models.dtos.file import FileDTO
from src.models.dtos.user import SimpleUserDTO


router = APIRouter(prefix='/api/files')


@router.get('')
def get_all(req: Request, res: Response):
    
    return files.get_all(req)


@router.post('')
async def post(req: Request, file: List[UploadFile]):
    
    return await files.create(req, file)


@router.delete('')
def delete(dto: FileDTO, req: Request, res: Response):
    
    return files.delete(dto, req)


@router.get('/download')
def get(dto: FileDTO, req: Request, res: Response):
    
    return files.get(dto, req)


@router.get('/share')
def get(dto: FileDTO, req: Request, res: Response):
    
    return files.share.get_all(dto, req)


@router.post('/share')
def post(dto: FileDTO, req: Request):
    
    return files.share.create(dto, req)
