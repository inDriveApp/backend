from fastapi import HTTPException

from src.core import database
from src.models.database.user import User
from src.models.dtos.login import LoginDTO


def buscar(): 
    db = database.connect()
    usuarios = db.execute('SELECT id, name, status FROM public.user ORDER BY name').all()
    
    if not usuarios:
        return []
    
    retorno = []
    for usuario in usuarios:
        usr = {
            'id': usuario['id'],
            'name': usuario['name'],
            'status': usuario['status']
        }
        
        retorno.append(usr)
    
    return retorno


def salvar(dto: LoginDTO):    
    db = database.connect()
    usuario = db.execute(
        'SELECT id, login, password FROM public.user WHERE login=:login AND password=passwd',
        {
            'login': dto.login,
            'passwd': dto.password
        }
        ).first()
    
    if not usuario:
        raise HTTPException(
            status_code=400,
            detail="Erro: Usuario ou Senha incorretos")
    
    retorno = {
        'id': usuario['id']
    }
    
    return retorno
