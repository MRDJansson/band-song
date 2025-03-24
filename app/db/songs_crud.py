from fastapi import HTTPException
from ..db.models import SongIn, SongOut

songs = [
    {"id": 0, "title": "Hatebreed", "artist": "Children of Bodom"},
    {"id": 1, "title": "Hellfire", "artist": "Lorna Shore"},
    {"id": 2, "title": "DEMOLISHER", "artist": "Slaughter to Prevail"},
]

def list_all_songs(artist: str = ""):
    if artist == "":
        return songs
    return [s for s in songs if s["artist"] == artist]

def list_song_by_id(song_id: int):
    sid = [s for s in songs if s["id"] == song_id]
    if len(sid) == 0:
        raise HTTPException(
    status_code=404, detail=f"Release with the ID of: {song_id} was not found."
    )
    return sid[0]

def save_song(song_in: SongIn):
    new_id = len(songs)
    song = SongOut(**song_in.model_dump(), id=new_id)
    songs.append(song.model_dump())
    return song

def delete_song_by_id(song_id: int):
    sid = [s for s in songs if s["id"] == song_id]
    if len(sid) == 0:
        raise HTTPException(
            status_code=404, detail=f"Release with the ID of: {song_id} was not found."
        )
    del songs[song_id]
    return {"message": f"Band with the ID of {song_id} was deleted."}