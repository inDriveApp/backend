from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.core.database import Base


class ModelBase(Base):

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    updated = Column(DateTime, server_onupdate=func.now())
    created = Column(DateTime, server_default=func.now())
