
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ARRAY, FLOAT
from sqlalchemy.orm import relationship

from .database import Base

class Order(Base):
    __tablename__ = 'order'

    order_id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default='open')
    items = Column(ARRAY(String))
    amount = Column(FLOAT)
    