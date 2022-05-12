import os

from datetime import datetime


def get_all(user:str): 
    # files_path = [os.path.abspath(x) for x in os.listdir(f'/home/{user}')]
    files_name = os.listdir(f'/home/{user}')
    
    retorno = []
    for file in files_name:
        f = {
            'name': file,
            'size': 0,
            'uploaded': datetime.now()
        }
        
        retorno.append(f)
    
    return retorno
