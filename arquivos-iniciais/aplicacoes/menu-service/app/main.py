from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.api import crud, models, schemas
from app.api.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/menu', response_model=list[schemas.Menu])
async def get_menu(db: Session = Depends(get_db)):
    data = crud.get_menu(db)
    return data

@app.post('/menu', response_model=schemas.Menu)
async def create_item_menu(menu: schemas.Menu, db: Session = Depends(get_db)):
    data = crud.create_item_menu(db=db, menu=menu)
    return data

@app.get('/menu/{item_id}', response_model=schemas.Menu)
async def get_menu_by_id(item_id: int, db: Session = Depends(get_db)):
    data = crud.get_menu_by_id(db=db, item_id=item_id)
    return data
    
@app.put('/menu/{item_id}', response_model=schemas.Menu)
async def update_item(item_id: int, menu_data: schemas.Menu, db: Session = Depends(get_db)):
    data = crud.update_item(db=db, item_id=item_id, menu_data=menu_data)
    return data

@app.delete('/menu/{item_id}', response_model=None)
async def delete_menu(item_id: int, db: Session = Depends(get_db)):
    db_delete = crud.delete_menu(db=db, item_id=item_id)
    return db_delete

    