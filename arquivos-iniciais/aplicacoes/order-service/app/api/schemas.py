from pydantic import BaseModel
from typing import Optional, List
from sqlmodel import Field

class Order(BaseModel):
    order_id: Optional[int]
    status: str
    items: Optional[List[str]]
    amount: Optional[float]

    class Config:
        orm_mode = True

class OrderUpdate(Order):
    pass
    
