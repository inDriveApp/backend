from os.path import exists

from fastapi import HTTPException, Request
from fastapi.responses import FileResponse

from src.models.dtos.file import FileDTO
from src.utils.functions import validate_file_request


def get(dto: FileDTO, req: Request):
    root_path = validate_file_request(req)
    
    path =  f'/home/{dto.path}' or f'{root_path}/{dto.name}'
    
    if path and not exists(path):
        raise HTTPException(
            status_code=400,
            detail='Arquivo solicitado não existe'
        )
    
    
    return FileResponse(path=path, filename=dto.name)
