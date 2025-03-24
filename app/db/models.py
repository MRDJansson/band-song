from sqlmodel import SQLModel, Field

class BaseSong(SQLModel):
    title: str
    artist: str
    
class SongIn(BaseSong):
    pass

class SongOut(BaseSong):
    id: int
    
class BandBase(SQLModel):
    name: str
    
class BandIn(BandBase):
    pass

class BandOut(BandBase):
    id: int

class BandDb(BaseSong, table=True):
    id: int = Field(default=None, primary_key=True)