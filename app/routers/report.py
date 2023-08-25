from collections import defaultdict
from fastapi import Depends, APIRouter

from app.db import get_fake_db
from app.routers.distributions import Distribution
from app.routers.donations import Donation

router = APIRouter()

def label_kv_in_donation_dict(balances):
    return [{"category": key, "quantity": value} for key, value in balances.items()]


@router.get("/balances/")
async def get_balances(db: dict = Depends(get_fake_db)) -> list[dict]:
    """
    This returns a summary of the balances in each category of
    resource the shelter has.
    """
    balances = defaultdict(float)
    donation_entry: Donation
    for donation_entry in db["donations"]:
        balances[donation_entry.donation_type] += donation_entry.units_donated

    distribution_entry: Distribution
    for distribution_entry in db["distributions"]:
        balances[distribution_entry.donation_type] -= distribution_entry.units_distributed

    return label_kv_in_donation_dict(balances)


@router.get("/donor-records/")
async def get_donor_records(db: dict = Depends(get_fake_db)) -> list:
    """
    This returns a summary of resources that each donor has given.
    """
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