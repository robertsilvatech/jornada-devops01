from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status, Response
from fastapi.responses import JSONResponse

def get_menu(db: Session):
    data = db.query(models.Menu).all()
    return data

def create_item_menu(db: Session, menu: schemas.Menu):
    data = models.Menu(name=menu.name, price=menu.price)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data 

def get_menu_by_id(db: Session, item_id: id):
    data = db.query(models.Menu).filter(models.Menu.item_id == item_id).first()
    if data:
        return data
    else:
        msg = {"message": f'Menu id {item_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)
    
def update_item(db: Session, item_id: int ,menu_data: schemas.Menu):
    data = db.query(models.Menu).filter(models.Menu.item_id == item_id).first()
    if data:
        if menu_data.name:
            data.name = menu_data.name
        if menu_data.price:
            data.price = menu_data.price
        db.commit()
        db.refresh(data)
        return data
    else:
        msg = {"message": f'Menu - item id {item_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)        

def delete_menu(db: Session, item_id: id):
    menu = db.query(models.Menu).filter(models.Menu.item_id == item_id).first()
    if menu:
        db.query(models.Menu).filter(models.Menu.item_id == item_id).delete()
        db.commit()
        return {"message": f'Menu {item_id} is deleted'}
    else:
        msg = {"message": f'Menu id {item_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)