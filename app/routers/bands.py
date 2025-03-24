from fastapi import APIRouter, status
from ..db.models import BandIn, BandOut
from ..db import bands_crud

router = APIRouter(prefix="/authors", tags=["authors"])

@router.get("/", response_model=list[BandOut])
def list_all_bands(name: str = ""):
    return bands_crud.list_all_bands(name)

@router.get("/{band_id}", response_model=BandOut)
def list_bands_by_id(band_id: int):
    return bands_crud.list_all_bands(band_id)

