from .dto_base import DTOBase


class LoginDTO(DTOBase):
    
    login: str
    password: str
