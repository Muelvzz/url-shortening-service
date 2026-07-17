from fastapi import APIRouter, status, HTTPException
from typing import List

from ..db import database
from ..schemas.url_schema import UrlCreate, UrlOut

router = APIRouter()

def show_error(e):
  print(f"Error occured: {e}")
  raise HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="an error occured..."
  )

@router.post("/shorten", status_code=status.HTTP_201_CREATED, response_model=UrlOut)
async def create_shorten_url(payload: UrlCreate):
  try:
    insert_url_from_db = database.insert_url(payload.url)
    return insert_url_from_db
  
  except Exception as e:
    show_error(e)

@router.get("/url/all", status_code=status.HTTP_202_ACCEPTED, response_model=List[UrlOut])
async def get_all_url():
  try:
    all_url = database.view_all_urls()
    return all_url
  
  except Exception as e:
    show_error(e)

@router.get("/url/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UrlOut)
async def select_url(id: int):
  try:
    selected_url = database.view_selected_url(id)
    return selected_url
  
  except Exception as e:
    show_error(e)