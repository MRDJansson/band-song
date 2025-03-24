from fastapi import HTTPException
from ..db.models import BandIn, BandOut

bands = [
    {"id": 0, "name": "Children of Bodom"},
    {"id": 1, "name": "Lorna Shore"},
]

def list_all_bands(name: str = ""):
    if name == "":
        return bands
    return [b for b in bands if b["name"] == name]


def list_band_by_id(band_id: int):
    bid = [b for b in bands if b["id"] == band_id]
    if len(bid) == 0:
        raise HTTPException(
            status_code=404, detail=f"Band with the iID of: {band_id} was not found."
        )
    return bid[0]

def save_band(band_in: BandIn):
    new_id = len(bands)
    band = BandOut(**band_in.model_dump(), id=new_id)
    bands.append(band.model_dump())
    return band

def delete_band_by_id(band_id: int):
    bid = [b for b in bands if b["id"] == band_id]
    if len(bid) == 0:
        raise HTTPException(
            status_code=404, detail=f"Band with the iID of: {band_id} was not found."
        )
    del bands[band_id]
    return {"message": f"Band with the ID of {band_id} was deleted."}