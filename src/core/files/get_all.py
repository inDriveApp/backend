from os import listdir, path
from datetime import datetime

from fastapi import HTTPException, Request

from src.utils.functions import convert_size


def get_all(req: Request):
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
    
    files_name = listdir(root_path)
    
    retorno = []
    for file in files_name:
        file_dir = req.headers['X-User']
        file_name = file
        file_path = f'/home/{file_dir}/{file_name}'
        
        f = {
            'name': file_name,
            'owner': file_dir,
            'size': convert_size(path.getsize(file_path)),
            'uploaded': int(path.getmtime(file_path)),
            'extension': None
        }
        
        if path.isdir(file_path):
            f['extension'] = 'directory'
        elif '.' in file_name:
            extension = file_name.split('.')
            
            if file_name[0] == '.' and len(extension) > 2:
                f['extension'] = extension[-1]
            elif file_name[0] != '.' and len(extension) > 1:
                f['extension'] = extension[-1]
        
        retorno.append(f)
    
    return retorno
