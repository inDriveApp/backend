from os import path, remove
from shutil import rmtree

from fastapi import HTTPException, Request

from src.models.dtos.file import FileDTO


def delete(dto: FileDTO, req: Request):
    if 'X-User' not in req.headers:
        raise HTTPException(
            status_code=400,
            detail='Usuario não informado'
        )
    
    user = req.headers['X-User']
    root_path = f'/home/{user}'

    if not path.exists(root_path):
        raise HTTPException(
            status_code=400,
            detail='Usuario informado não existe'
        )
    
    if not path.exists(f'{root_path}/{dto.name}'):
        raise HTTPException(
            status_code=400,
            detail='Arquivo não existe'
        )
    
    remove(f'{root_path}/{dto.name}')
    
    return 'OK'
