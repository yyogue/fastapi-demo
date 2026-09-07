from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from models.item import Item
from controllers import item_controller

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=Item)
def create_item(item: Item, session: Session = Depends(get_session)):
    return item_controller.create_item(item, session)

@router.get("/", response_model=list[Item])
def list_items(session: Session = Depends(get_session)):
    return item_controller.get_all_items(session)

@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int, session: Session = Depends(get_session)):
    return item_controller.get_item_by_id(item_id, session)

@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item, session: Session = Depends(get_session)):
    return item_controller.update_item(item_id, item, session)

@router.delete("/{item_id}")
def delete_item(item_id: int, session: Session = Depends(get_session)):
    return item_controller.delete_item(item_id, session)
