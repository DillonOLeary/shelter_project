from collections import defaultdict
from pydantic import BaseModel, ConfigDict, validator
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware


def to_camel(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app_db = None


def get_db():
    global app_db
    if app_db == None:
        app_db = defaultdict(list)
    return app_db


class Donation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    donor_name: str
    donation_type: str
    units_donated: float
    donation_date: str

    @validator("donor_name", "donation_type", pre=True)
    def to_lowercase(cls, value: str):
        return value.lower()


class Distribution(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    donation_type: str
    units_distributed: float
    distribution_date: str

    @validator("donation_type", pre=True)
    def to_lowercase(cls, value: str):
        return value.lower()


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
    """
    This endpoint only exists for testing
    """
    return db


def label_kv_in_donation_dict(balances):
    return [{"category": key, "quantity": value} for key, value in balances.items()]


@app.get("/balances/")
async def get_balances(db: dict = Depends(get_db)) -> list[dict]:
    balances = defaultdict(float)
    donation_entry: Donation
    for donation_entry in db["donations"]:
        balances[donation_entry.donation_type] += donation_entry.units_donated

    distribution_entry: Distribution
    for distribution_entry in db["distributions"]:
        balances[distribution_entry.donation_type] -= distribution_entry.units_distributed

    return label_kv_in_donation_dict(balances)


@app.get("/donor-records/")
async def get_donor_records(db: dict = Depends(get_db)) -> list:
    # TODO refactor - this is a dictionary of donors with all their balances for each category of donation
    donor_records = defaultdict(lambda: defaultdict(float))
    donation_entry: Donation
    for donation_entry in db["donations"]:
        donor_records[donation_entry.donor_name][donation_entry.donation_type] += donation_entry.units_donated

    result_list = []
    for donor, donor_contributions in donor_records.items():
        result_list.append({
            "donor": donor,
            "record": label_kv_in_donation_dict(donor_contributions)
        })

    return result_list


# for debugging purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
