from os import listdir, path
from datetime import datetime

from fastapi import HTTPException, Request

from src.utils.functions import convert_size, validate_file_request


def get_all(req: Request):
    root_path = validate_file_request(req)
    files_name = listdir(root_path)
    
    retorno = []
    for file in files_name:
        f = {
            'name': file,
            'size': convert_size(path.getsize(f'{root_path}/{file}')),
            'uploaded': int(path.getmtime(f'{root_path}/{file}')),
            'extension': None
        }
        
        if path.isdir(f'{root_path}/{file}'):
            f['extension'] = 'directory'
        elif '.' in file:
            extension = file.split('.')
            
            if file[0] == '.' and len(extension) > 2:
                f['extension'] = extension[-1]
            elif file[0] != '.' and len(extension) > 1:
                f['extension'] = extension[-1]
        
        retorno.append(f)
    
    return retorno
