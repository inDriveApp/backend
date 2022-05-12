import aiofiles
from typing import List, Optional
from fastapi import APIRouter, File, HTTPException, Request, Response, UploadFile

from src.core import files
from src.models.dtos.user import SimpleUserDTO
from typing import List


router = APIRouter(prefix='/api/files')


@router.get('')
def get_all(dto: SimpleUserDTO, req: Request, res: Response):
    
    return files.get_all(dto.login)


@router.post('')
async def post(req: Request, file: List[UploadFile]):
    
    return await files.create(req, file)
