from datetime import datetime
from typing import Optional

from .dto_base import DTOBase


class FileDTO(DTOBase):
    
    name: str
    path: Optional[str]
