from os.path import exists

from fastapi import HTTPException, Request
from fastapi.responses import FileResponse

from src.models.dtos.file import FileDTO
from src.utils.functions import validate_file_request


def get(dto: FileDTO, req: Request):
    root_path = validate_file_request(req)
    
    if dto.path and exists(dto.path):
        path = f'{dto.path}'
    elif exists(root_path):
        path = f'{root_path}/{dto.name}'
    else:
        raise HTTPException(
            status_code=400,
            detail='Usuario informado não existe'
        )
    
    return FileResponse(path=path, filename=dto.name)
