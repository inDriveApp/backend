import bcrypt
from fastapi import HTTPException

from src.core import database
from src.models.database.user import User
from src.models.dtos.login import LoginDTO


def create(dto: LoginDTO):    
    db = database.connect()

    usuario = db.execute(
        'SELECT id, login, password FROM public.user WHERE login=:login',
        {
            'login': dto.login
        }
        ).first()
    
    if not usuario:
        raise HTTPException(
            status_code=400,
            detail='Erro: Usuario ou Senha incorretos'
        )
    
    check_password = bcrypt.checkpw(
        dto.password.encode('utf-8'),
        usuario['password'].encode('utf-8')
    )

    if not check_password:
        raise HTTPException(
            status_code=400,
            detail='Erro: Usuario ou Senha incorretos'
        )
    
    retorno = {
        'id': usuario['id']
    }
    
    return retorno
