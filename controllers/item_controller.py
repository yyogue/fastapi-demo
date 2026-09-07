from sqlmodel import Session, select
from fastapi import HTTPException
from models.item import Item


def create_item(item: Item, session: Session):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_all_items(session: Session):
    return session.exec(select(Item)).all()

def get_item_by_id(item_id: int, session: Session):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

def update_item(item_id: int, updated: Item,session: Session):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = updated.name
    item.price = updated.price
    item.is_available = updated.is_available
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def delete_item(item_id: int, session: Session):
    item = session.get(Item, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()
    return { "oka": True }