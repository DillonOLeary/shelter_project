from fastapi import Depends, APIRouter
from pydantic import BaseModel, ConfigDict, validator

from app.db import get_fake_db
from app.utils import to_camel

router = APIRouter()

class Distribution(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    donation_type: str
    units_distributed: float
    distribution_date: str

    @validator("donation_type", pre=True)
    def to_lowercase(cls, value: str):
        return value.lower()


@router.post("/distributions/")
async def register_distribution(distribution: Distribution, db: dict = Depends(get_fake_db)) -> Distribution:
    """
    Register the distribution of resources from the shelter. This will subtract from the balance for
    the category that was distributed.
    """
    db["distributions"].append(distribution)
    return distribution