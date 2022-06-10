from os.path import exists
import math

from fastapi import HTTPException, Request


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0 B"
   
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   
   return "%s %s" % (s, size_name[i])


def validate_file_request(req: Request):
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

    return root_path
