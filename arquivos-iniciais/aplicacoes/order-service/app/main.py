from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.api import crud, models, schemas
from app.api.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/orders/', response_model=list[schemas.Order])
def get_orders(db: Session = Depends(get_db)):
    orders = crud.get_orders(db)
    return orders

@app.get('/order/{order_id}', response_model=schemas.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    get_order = crud.get_order(db=db, order_id=order_id)
    return get_order

@app.get('/order/{order_id}/detail', response_model=None)
def get_order(order_id: int, db: Session = Depends(get_db)):
    data = crud.get_order_detail(db=db, order_id=order_id)
    return data

@app.post('/order', response_model=schemas.Order)
def create_order(order: schemas.Order, db: Session = Depends(get_db)):
    db_order = crud.create_order(db=db, order=order)
    return db_order

@app.put('/order/{order_id}', response_model=None)
def update_order(order_id: int, order_data: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_update = crud.update_order(db=db, order_id=order_id ,order_data=order_data)
    return order_update

@app.delete('/order/{order_id}', response_model=None)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_order(db=db, order_id=order_id)
    return db_delete