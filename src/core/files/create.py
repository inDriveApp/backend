from os.path import exists
from typing import List

import aiofiles
from fastapi import HTTPException, Request, UploadFile


async def create(files: List[UploadFile], req: Request):
    if 'X-User' not in req.headers:
        raise HTTPException(
            status_code=400,
            detail='Usuario não informado'
        )
    
    user = req.headers['X-User']
    root_path = f'/home/{user}'

    if not exists(root_path):
        raise HTTPException(
            status_code=400,
            detail='Usuario informado não existe'
        )
    
    for file in files:
        destin_file = f'{root_path}/{file.filename}'
        
        async with aiofiles.open(destin_file, 'wb') as out_file:
            while content := await file.read(1024):
                await out_file.write(content)
    
    return {'Result': 'OK', 'filenames': [file.filename for file in files]}
