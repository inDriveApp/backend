from typing import List
import uuid

from fastapi import HTTPException, Request

from src.core import database
from src.models.dtos.file import FileDTO
from src.models.database.share import Share


def create(dto: FileDTO, req: Request):
    if not dto.user:
        raise HTTPException(
            status_code=400,
            detail='Usuario não informado'
        )
    
    if 'X-User' not in req.headers:
        raise HTTPException(
            status_code=400,
            detail='Usuario não informado'
        )
    
    db = database.connect()
    
    user = db.execute(
        'SELECT id, name FROM public.user WHERE id=:id',
        {
            'id': dto.user
        }
    ).first()
    
    if not user:
        raise HTTPException(
            status_code=400,
            detail='Usuário informado não existe no banco'
        )
    
    owner_id = req.headers['X-User']
    
    owner = db.execute(
        'SELECT id, name FROM public.user WHERE id=:id',
        {
            'id': owner_id
        }
    ).first()

    if not owner:
        raise HTTPException(
            status_code=400,
            detail='Dono do arquivo informado não existe no banco'
        )
    
    share_dict = {
        'id': uuid.uuid4(),
        'file': dto.name,
        'owner': owner_id,
        'user': dto.user,
        'status': 1
    }
    
    share = Share(**share_dict)
    
    try:
        db.add(share)
        db.commit()
        db.refresh(share)
    except Exception as e:
        db.rollback()
        print(e)
        
        raise HTTPException(
            status_code=400,
            detail='Não foi possivel salvar o compartilhamento'
        )
    
    return 'OK'