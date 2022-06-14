from os import listdir, path
from datetime import datetime

from fastapi import HTTPException, Request

from src.core import database
from src.utils.functions import convert_size


def get_all(req: Request):    
    db = database.connect()
    
    files = db.execute(
        """SELECT DISTINCT s.file,
                s.owner
           FROM public.share s
           WHERE s.user = :id
                 AND s.status = 1""",
        {
            'id': req.headers['X-User']
        }
    ).all()
    
    if not files:
        return []
    
    retorno = []
    for file in files:
        file_dir = file['owner']
        file_name = file['file']
        file_path = f'/home/{file_dir}/{file_name}'
        
        if not path.exists(file_path):
            continue
        
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
