from datetime import datetime

from .dto_base import DTOBase


class FileDTO(DTOBase):
    
    name: str
    size: float
    uploaded: datetime
