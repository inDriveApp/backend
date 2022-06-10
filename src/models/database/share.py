from sqlalchemy import Column, Integer, String, text
from sqlalchemy.dialects.postgresql import UUID

from .model_base import ModelBase


class Share(ModelBase):

    __tablename__ = 'share'

    file = Column(String(500), nullable=False)
    owner = Column(UUID(as_uuid=True), nullable=False)
    user = Column(UUID(as_uuid=True), nullable=False)
    status = Column(Integer, server_default=text('0'))  # [ Inativo, Ativo ]
