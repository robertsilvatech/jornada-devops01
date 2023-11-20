from pydantic import BaseModel
from typing import Optional, List
from sqlmodel import Field

class Menu(BaseModel):
    item_id: Optional[int]
    name: str
    price: Optional[float]

    class Config:
        orm_mode = True