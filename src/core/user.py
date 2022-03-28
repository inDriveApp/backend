import uuid
import bcrypt
from fastapi import HTTPException
from pydantic import UUID4

from src.core import database
from src.models.database.user import User
from src.models.dtos.user import UserDTO


def get_all(): 
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
            detail="Erro: Já existe este usuario no sistema"
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
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(
            status_code=400,
            detail="Erro: Não foi possivel salvar o usuario."
        )
    
    retorno = {
        'id': user.id
    }
    
    return retorno    


def delete(id: UUID4):
    db = database.connect()
    user = db.execute(
        'SELECT id FROM public.user WHERE id=:id',
        {'id': id}
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Erro: Usuário não existe"
        )

    try:
        db.execute(
            'DELETE FROM public.user where id=:id',
            {'id':id}
        )
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(
            status_code=400,
            detail="Erro: Não foi possivel deletar o usuario."
        )
    
    return 'Usuário removido com sucesso!'
