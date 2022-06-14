from typing import List
from fastapi import APIRouter, HTTPException, Request, Response, UploadFile

from src.core import files
from src.models.dtos.file import FileDTO
from src.models.dtos.user import SimpleUserDTO


router = APIRouter(prefix='/api/files')


@router.get('')
def get_all(req: Request):
    
    return files.get_all(req)


@router.post('')
async def post(file: List[UploadFile], req: Request):
    
    return await files.create(file, req)


@router.delete('')
def delete(dto: FileDTO, req: Request):
    
    return files.delete(dto, req)


@router.get('/download/{file}')
def get(file: str, req: Request):
    
    return files.get(file, req)


@router.get('/share')
def get(req: Request):
    
    return files.share.get_all(req)


@router.post('/share')
def post(dto: FileDTO, req: Request):
    
    return files.share.create(dto, req)
