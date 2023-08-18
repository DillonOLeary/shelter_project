from collections import defaultdict
from pydantic import BaseModel
import uvicorn
from fastapi import Depends, FastAPI


app = FastAPI(
    title="Shelter",
    summary="This project is a basic donation inventory management application.",
    version="0.0.1",
    contact={
        "name": "Dillon",
        "email": "dillon.oleary@icloud.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    },
)

app_db = None


def get_db():
    global app_db
    if app_db == None:
        app_db = defaultdict(list)
    return app_db


class Donation(BaseModel):
    donor_name: str
    donation_type: str
    units_donated: float
    donation_date: str


class Distribution(BaseModel):
    donation_type: str
    units_distributed: float
    distributed_date: str


@app.post("/donations/")
async def register_donation(donation: Donation, db: dict = Depends(get_db)) -> Donation:
    db["donations"].append(donation)
    return donation


@app.post("/distributions/")
async def register_distribution(distribution: Distribution, db: dict = Depends(get_db)) -> Distribution:
    db["distributions"].append(distribution)
    return distribution


@app.get("/database/")
async def get_full_database(db: dict = Depends(get_db)) -> dict:
    return db


@app.get("/balances/")
async def get_balances(db: dict = Depends(get_db)) -> dict:
    balances = defaultdict(float)
    donation_entry: Donation
    for donation_entry in db["donations"]:
        balances[donation_entry.donation_type] += donation_entry.units_donated

    distribution_entry: Distribution
    for distribution_entry in db["distributions"]:
        balances[distribution_entry.donation_type] -= distribution_entry.units_distributed

    return {"balances": balances}


# for debugging purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
