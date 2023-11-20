
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY, FLOAT
from sqlalchemy.orm import relationship

from .database import Base

class Menu(Base):
    __tablename__ = 'menu'

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(FLOAT)
    