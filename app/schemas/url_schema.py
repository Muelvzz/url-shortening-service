from pydantic import BaseModel
from datetime import datetime

class UrlBase(BaseModel):
  url: str
  shortcode: str
  updated_at: datetime


class UrlCreate(BaseModel):
  url: str


class UrlOut(UrlBase):
  id: int
  access_count: int
  created_at: datetime