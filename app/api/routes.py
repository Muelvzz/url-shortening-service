from fastapi import APIRouter, status

from ..db.database import insert_url
from ..schemas.url_schema import UrlCreate, UrlOut

router = APIRouter()

@router.post("/shorten", status_code=status.HTTP_201_CREATED, response_model=UrlOut)
async def create_shorten_url(payload: UrlCreate):
  insert_url_from_db = insert_url(payload.url)

  return insert_url_from_db