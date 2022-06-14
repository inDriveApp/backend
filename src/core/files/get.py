from os.path import exists

from fastapi import HTTPException, Request
from fastapi.responses import FileResponse

from src.models.dtos.file import FileDTO


def get(file: str, req: Request):
    if 'X-Owner' not in req.headers:
        raise HTTPException(
            status_code=400,
            detail='Proprietario do arquivo não informado'
        )
    
    owner = req.headers['X-Owner']
    
    path = f'/home/{owner}/{file}'
    
    if path and not exists(path):
        raise HTTPException(
            status_code=400,
            detail='Arquivo solicitado não existe'
        )
    
    return FileResponse(path=path, filename=file)
