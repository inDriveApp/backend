from typing import List
import aiofiles
from fastapi import File, HTTPException, Request, UploadFile


async def create(req: Request, files: List[UploadFile]):

    if 'user' not in req.headers:
        raise HTTPException(
            status_code=400,
            detail='Usuario não informado'
        )
    
    user = req.headers['user']
    
    for file in files:
        destin_file = f'/home/{user}/' + file.filename
        
        async with aiofiles.open(destin_file, 'wb') as out_file:
            while content := await file.read(1024):
                await out_file.write(content)
    
    return {'Result': 'OK', 'filenames': [file.filename for file in files]}
