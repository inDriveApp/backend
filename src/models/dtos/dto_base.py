from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID


class DTOBase(BaseModel):
    
    id: Optional[UUID]
    
    # * Classe responsável por configurar uma limpeza nos campos de string
    # * removendo espaços vazios ao final (strip())
    # * Usando em conjunto com constr(min_length=1)
    # * garante que post com somente espaços vazios não preencha campos obrigatorios
    class Config():
        anystr_strip_whitespace = True
