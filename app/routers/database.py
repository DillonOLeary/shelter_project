from fastapi import APIRouter, Depends

from app.db import get_fake_db

router = APIRouter()


@router.get("/database/")
async def get_full_database(db: dict = Depends(get_fake_db)) -> dict:
    """
    This endpoint only exists for testing
    """
    return db
