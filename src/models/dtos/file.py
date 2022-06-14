from datetime import datetime
from typing import Optional

from pydantic.types import UUID

from .dto_base import DTOBase


class FileDTO(DTOBase):
    
    name: str
    user: Optional[UUID]
