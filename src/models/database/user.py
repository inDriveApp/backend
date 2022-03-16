from sqlalchemy import Column, Integer, String, text

from .model_base import ModelBase


class User(ModelBase):

    __tablename__ = 'user'

    login = Column(String(32), nullable=False)
    name = Column(String(100), nullable=False)
    password = Column(String(32), nullable=False)
    status = Column(Integer, server_default=text('0'))  # [ Inativo, Ativo ]
