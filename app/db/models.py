# from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import List

class BaseSong(BaseModel):
    titles: str
    artist: str
    formed: int
    
class SongIn(BaseSong):
    pass

class SongOut(BaseSong):
    id: int
    
class BandBase(BaseModel):
    name: str
    
class BandIn(BandBase):
    pass

class BandOut(BandBase):
    id: int

# class BandDb(BaseSong, table=True):
#     id: int = Field(default=None, primary_key=True)