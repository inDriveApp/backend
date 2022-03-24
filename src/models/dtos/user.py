from typing import Optional
from .dto_base import DTOBase


class UserDTO(DTOBase):
    
    name: Optional[str]
    login: str
    password: str
