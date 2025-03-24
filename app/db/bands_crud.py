from fastapi import HTTPException
from ..db.models import BandIn, BandOut

bands = [
    {"id": "name": "Children of Bodom"},
    {"id": "name": "Lorna Shore"},
]

def read_all_bands(name: str = ""):
    if name == "":
        return bands
    return [b for b in bands if b["name"] == name]


def read_band_by_id(band_id: int):
    bid = [b for b in bands if b["id"] == band_id]
    if len(bid) == 0:
        raise HTTPException(
            status_code=404, detail=f"Band with the iID of: {band_id} was not found."
        )
    return bid[0]

