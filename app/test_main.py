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
            "donorName": "phil",
            "donationType": "money",
            "unitsDonated": "5",
            "donationDate": "2008-09-15"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "donorName": "phil",
        "donationType": "money",
        "unitsDonated": 5.0,
        "donationDate": "2008-09-15"
    }


def test_post_distribution():
    response = client.post(
        "/distributions/",
        json={
            "donationType": "money",
            "unitsDistributed": "5",
            "distributionDate": "2015-03-20"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "donationType": "money",
        "unitsDistributed": 5.0,
        "distributionDate": "2015-03-20"
    }


def test_post_bad_donation():
    response = client.post(
        "/donations/",
        json={
            "donorName": "phil",
            "unitsDonated": "5",
            "donationDate": "2008-09-15"
        }
    )
    assert response.status_code == 422


def test_get_full_database():
    client.post(
        "/donations/",
        json={
            "donorName": "sasha",
            "donationType": "clothes",
            "unitsDonated": "4",
            "donationDate": "2012-10-15"
        }
    )
    response = client.get("/database/")
    assert response.status_code == 200
    assert response.json() == {
        "donations": [
            {
                "donorName": "sasha",
                "donationType": "clothes",
                "unitsDonated": 4.0,
                "donationDate": "2012-10-15"
            }
        ]
    }


def test_generate_report():
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
            "donorName": "kristin",
            "donationType": "money",
            "unitsDonated": "3",
            "donationDate": "2022-02-23"
        }
    )
    client.post(
        "/donations/",
        json={
            "donorName": "sasha",
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
    response = client.get("/balances/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "category": "money",
            "quantity": 4.0
        },
        {
            "category": "clothes",
            "quantity": 2.0
        }
    ]
