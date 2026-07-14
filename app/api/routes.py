from fastapi import APIRouter, status, HTTPException

from ..db.database import insert_url
from ..schemas.url_schema import UrlCreate, UrlOut

router = APIRouter()

@router.post("/shorten", status_code=status.HTTP_201_CREATED, response_model=UrlOut)
async def create_shorten_url(payload: UrlCreate):
  try:
    insert_url_from_db = insert_url(payload.url)

    return insert_url_from_db
  
  except Exception as e:
    print(f"Error occured: {e}")
    raise HTTPException(
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
      detail="an error occured while shortening the URL..."
    )