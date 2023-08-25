from fastapi import APIRouter, Depends

from app.db import get_fake_db

router = APIRouter()


@router.get("/database/")
async def get_full_database(db: dict = Depends(get_fake_db)) -> dict:
    """
    Returns a dictionary with the entire database.
    
    This endpoint only exists for testing. It will not scale as the software
    grows.
    """
    return db
