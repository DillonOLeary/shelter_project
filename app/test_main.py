from collections import defaultdict
from fastapi.testclient import TestClient
import pytest
from .main import app, get_db

test_db = defaultdict(list)


def get_test_db() -> defaultdict:
    return test_db


app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # A test function will be run at this point
    yield
    global test_db
    test_db = defaultdict(list)


def test_post_donation():
    response = client.post(
        "/donations/",
        json={
            "donor_name": "phil",
            "donation_type": "money",
            "units_donated": "5",
            "donation_date": "2008-09-15"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "donor_name": "phil",
        "donation_type": "money",
        "units_donated": 5.0,
        "donation_date": "2008-09-15"
    }


def test_post_distribution():
    response = client.post(
        "/distributions/",
        json={
            "donation_type": "money",
            "units_distributed": "5",
            "distributed_date": "2015-03-20"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "donation_type": "money",
        "units_distributed": 5.0,
        "distributed_date": "2015-03-20"
    }


def test_post_bad_donation():
    response = client.post(
        "/donations/",
        json={
            "donor_name": "phil",
            "units_donated": "5",
            "donation_date": "2008-09-15"
        }
    )
    assert response.status_code == 422


def test_get_full_database():
    client.post(
        "/donations/",
        json={
            "donor_name": "sasha",
            "donation_type": "clothes",
            "units_donated": "4",
            "donation_date": "2012-10-15"
        }
    )
    response = client.get("/database/")
    assert response.status_code == 200
    assert response.json() == {
        "donations": [
            {
                "donor_name": "sasha",
                "donation_type": "clothes",
                "units_donated": 4.0,
                "donation_date": "2012-10-15"
            }
        ]
    }


def test_generate_report():
    client.post(
        "/donations/",
        json={
            "donor_name": "phil",
            "donation_type": "money",
            "units_donated": "5",
            "donation_date": "2008-09-15"
        }
    )
    client.post(
        "/donations/",
        json={
            "donor_name": "kristin",
            "donation_type": "money",
            "units_donated": "3",
            "donation_date": "2022-02-23"
        }
    )
    client.post(
        "/donations/",
        json={
            "donor_name": "sasha",
            "donation_type": "clothes",
            "units_donated": "2",
            "donation_date": "2012-10-15"
        }
    )
    client.post(
        "/distributions/",
        json={
            "donation_type": "money",
            "units_distributed": "4",
            "distributed_date": "2023-07-20"
        }
    )
    response = client.get("/balances/")
    assert response.status_code == 200
    assert response.json() == {
        "balances":
            {
                "money": 4.0,
                "clothes": 2.0
            }
    }
