from collections import defaultdict
from pydantic import BaseModel
import uvicorn
from fastapi import Depends, FastAPI

app = FastAPI()

app_db = None


def get_db():
    global app_db
    if app_db == None:
        app_db = defaultdict(list)
    return app_db


class Donation(BaseModel):
    donor_name: str
    donation_type: str
    units_donated: str
    donation_date: str


class Distribution(BaseModel):
    donation_type: str
    units_distributed: str
    distributed_date: str


@app.post("/donations/")
async def register_donation(donation: Donation, db: dict = Depends(get_db)) -> Donation:
    db["donations"].append(donation)
    return donation


@app.post("/distributions/")
async def register_donation(distribution: Distribution, db: dict = Depends(get_db)) -> Distribution:
    db["distributions"].append(distribution)
    return distribution


@app.get("/donations/")
async def get_donations(db: dict = Depends(get_db)):
    return db

# for debugging purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
