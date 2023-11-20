from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status, Response
from fastapi.responses import JSONResponse
import requests
from decouple import config

DATABASE_URL = config('MENU_SERVICE_URL')

def _check_item_exists(item_id):
    response = requests.get(f'{DATABASE_URL}/menu')
    if response.status_code == 200:
        content = response.json()
        mapping_itens = {item['item_id']: item for item in content}
        print(mapping_itens)
        get_item = mapping_itens.get(int(item_id))
        return get_item
    
def _get_items_detail():
    response = requests.get(f'{DATABASE_URL}/menu')
    if response.status_code == 200:
        content = response.json()
        mapping_itens = {item['item_id']: item for item in content}
        return mapping_itens    

def create_order(db: Session, order: schemas.Order):
    itens_not_found = []
    amount_from_menu = 0.0
    if order.items:
        for item in order.items:
            item_detail = _check_item_exists(item)
            if not item_detail:
                itens_not_found.append(item)
            else:
                amount_from_menu += item_detail['price']
    if len(itens_not_found) > 0:
        msg = {"message": f'Itens with id: {itens_not_found} not found in Menu, check your request'}
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=msg)
    else:
        db_order = models.Order(status=order.status, items=order.items, amount=amount_from_menu)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order 

def get_order(db: Session, order_id: id):
    db_order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if db_order:
        return db_order
    else: 
        msg = {"message": f'Order id {order_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)        

def get_order_detail(db: Session, order_id: id):
    data = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if data:
        items_from_menu = _get_items_detail()
        items_detail = []
        for item in data.items:
            get_detail = items_from_menu.get(int(item))
            if get_detail:
                items_detail.append(get_detail)
        result = {}
        result['order_id'] = data.order_id
        result['status'] = data.status
        result['items'] = items_detail
        result['amount'] = data.amount
        return result
    else: 
        msg = {"message": f'Order id {order_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)        

def delete_order(db: Session, order_id: id):
    order = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if order:
        db.query(models.Order).filter(models.Order.order_id == order_id).delete()
        db.commit()
        return {"message": f'Order {order_id} is deleted'}
    else:
        msg = {"message": f'Order id {order_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)
    
def update_order(db: Session, order_id: id, order_data: schemas.OrderUpdate):
    data = db.query(models.Order).filter(models.Order.order_id == order_id).first()
    if data:
        print(f'Data {data}')
        print(f'Data {data.status}')
        print(f'Order status {order_data.status}')
        if order_data.status:
            data.status = order_data.status
            print(f'Data {data.status} new')
        if order_data.items:
            data.items = order_data.items
            itens_not_found = []
            amount_from_menu = 0.0
            for item in order_data.items:
                item_detail = _check_item_exists(item)
                if not item_detail:
                    itens_not_found.append(item)
                else:
                    amount_from_menu += item_detail['price']
            if len(itens_not_found) > 0:
                msg = {"message": f'Itens with id: {itens_not_found} not found in Menu, check your request'}
                return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=msg)
            else:
                data.amount = amount_from_menu
        db.commit()
        db.refresh(data)
        return data     
    else:
        msg = {"message": f'Order id {order_id} not found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=msg)        

def get_orders(db: Session):
    data = db.query(models.Order).all()
    return data