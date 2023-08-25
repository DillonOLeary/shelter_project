from collections import defaultdict
from fastapi.testclient import TestClient
import pytest

from app.db import get_fake_db
from .main import app

test_db = defaultdict(list)


def get_test_db() -> defaultdict:
    return test_db


app.dependency_overrides[get_fake_db] = get_test_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # A test function will be run at this point
    yield
    global test_db
    test_db = defaultdict(list)


def generate_database():
    client.post(
        "/donations/",
        json={
            "donorName": "phil",
            "donationType": "money",
            "unitsDonated": "5",
            "donationDate": "2008-09-15"
        }
    )
    client.post(
        "/donations/",
        json={
            "donorName": "phil",
            "donationType": "money",
            "unitsDonated": "7",
            "donationDate": "2009-09-15"
        }
    )
    client.post(
        "/donations/",
        json={
            "donorName": "kristin",
            "donationType": "money",
            "unitsDonated": "3",
            "donationDate": "2022-02-23"
        }
    )
    client.post(
        "/donations/",
        json={
            "donorName": "phil",
            "donationType": "clothes",
            "unitsDonated": "2",
            "donationDate": "2012-10-15"
        }
    )
    client.post(
        "/distributions/",
        json={
            "donationType": "money",
            "unitsDistributed": "4",
            "distributionDate": "2023-07-20"
        }
    )
