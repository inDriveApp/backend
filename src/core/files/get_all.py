import os
from datetime import datetime

from fastapi import HTTPException, Request

from src.utils.functions import convert_size


def get_all(req: Request):
    if 'user' not in req.headers:
        raise HTTPException(
            status_code=400,
            detail='Erro: Usuario não informado'
        )
    
    user = req.headers['user']
    
    root_path = f'/home/{user}'
    files_name = os.listdir(root_path)
    
    retorno = []
    for file in files_name:
        
        f = {
            'name': file,
            'size': convert_size(os.path.getsize(f'{root_path}/{file}')),
            'uploaded': int(os.path.getmtime(f'{root_path}/{file}')),
            'extension': None
        }
        
        if os.path.isdir(f'{root_path}/{file}'):
            f['extension'] = 'directory'
        elif '.' in file:
            extension = file.split('.')
            
            if file[0] == '.' and len(extension) > 2:
                f['extension'] = extension[-1]
            elif file[0] != '.' and len(extension) > 1:
                f['extension'] = extension[-1]
        
        retorno.append(f)
    
    return retorno
