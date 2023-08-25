from fastapi import Depends, APIRouter
from pydantic import BaseModel, ConfigDict, validator

from app.db import get_fake_db
from app.utils import to_camel

router = APIRouter()

class Donation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    donor_name: str
    donation_type: str
    units_donated: float
    donation_date: str

    @validator("donor_name", "donation_type", pre=True)
    def to_lowercase(cls, value: str):
        return value.lower()


@router.post("/donations/")
async def register_donation(donation: Donation, db: dict = Depends(get_fake_db)) -> Donation:
    db["donations"].append(donation)
    return donation