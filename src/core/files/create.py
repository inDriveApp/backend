from typing import List

import aiofiles
from fastapi import Request, UploadFile

from src.utils.functions import validate_file_request


async def create(req: Request, files: List[UploadFile]):
    root_path = validate_file_request(req)
    
    for file in files:
        destin_file = f'{root_path}/{file.filename}'
        
        async with aiofiles.open(destin_file, 'wb') as out_file:
            while content := await file.read(1024):
                await out_file.write(content)
    
    return {'Result': 'OK', 'filenames': [file.filename for file in files]}
