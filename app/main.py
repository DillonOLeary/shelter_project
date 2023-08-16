import datetime
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()

class BaseDonation(BaseModel):
    donor_name: str
    donation_type: str
    units_donated: str
    donation_date: str

class DonationWithID(BaseDonation):
    timestamp: str

@app.post("/")
async def register_donation(donation: BaseDonation) -> DonationWithID:
    return {
        "donor_name": "phil",
        "donation_type": "money",
        "units_donated": "5",
        "donation_date": "2008-09-15",
        "timestamp": "12345"
    }

# for debugging purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
