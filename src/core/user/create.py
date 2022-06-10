from os import mkdir
import uuid

import bcrypt
from fastapi import HTTPException
from pydantic import UUID4

from src.core import database
from src.models.database.user import User
from src.models.dtos.user import UserDTO


def create(dto: UserDTO):
    db = database.connect()
    user = db.execute(
        'SELECT id, name FROM public.user WHERE login=:login',
        {
            'login': dto.login
        }
    ).first()
    
    if user:
        raise HTTPException(
            status_code=400,
            detail='Erro: Já existe este usuario no sistema'
        )

    user_dict = {
        'id': uuid.uuid4(),
        'name': dto.name,
        'login': dto.login,
        'password': bcrypt.hashpw(
            dto.password.encode(
                'utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8', 'ignore'),
        'status': 1
    }

    user = User(**user_dict)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        
        mkdir(f'/home/{user_dict["id"]}')
    except Exception as e:
        db.rollback()
        print(e)
        
        raise HTTPException(
            status_code=400,
            detail='Erro: Não foi possivel salvar o usuario.'
        )
    
    retorno = {
        'id': user.id
    }
    
    return retorno    
