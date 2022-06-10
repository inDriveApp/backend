from os import path, remove
from shutil import rmtree

from fastapi import HTTPException, Request

from src.models.dtos.file import FileDTO
from src.utils.functions import validate_file_request


# TODO
def delete(dto: FileDTO, req: Request):
    root_path = validate_file_request(req)
    
    if not path.exists(f'{root_path}/{dto.name}'):
        raise HTTPException(
            status_code=400,
            detail='Arquivo não existe'
        )
    
    remove(f'{root_path}/{dto.name}')
    
    return 'OK'
