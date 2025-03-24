from fastapi import APIRouter, status
from ..db.models import SongIn, SongOut
from ..db import songs_crud

router = APIRouter(prefix="/songs", tags=["songs"])

@router.get("/", response_model=list[SongOut])
def list_all_songs(song: str = ""):
    return songs_crud.list_all_songs(song)

@router.get("/{song_id}", response_model=SongOut)
def list_all_songs_by_id(song_id: int):
    return songs_crud.list_song_by_id(song_id)

@router.post("/", response_model=SongOut, status_code=status.HTTP_201_CREATED)
def save_song(song_in: SongIn):
    return songs_crud.save_song(song_in)

@router.delete("/{song_id}")
def delete_song_by_id(song_id: int):
    return songs_crud.delete_song_by_id(song_id)