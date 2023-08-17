from collections import defaultdict
from fastapi.testclient import TestClient
from .main import app, get_db

test_db = defaultdict(list)


def get_test_db() -> defaultdict:
    return test_db


def teardown():
    global test_db
    test_db = defaultdict(list)


app.dependency_overrides[get_db] = get_test_db

client = TestClient(app)


def test_post_donation():
    response = client.post(
        "/",
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
        "units_donated": "5",
        "donation_date": "2008-09-15"
    }

    teardown()


def test_post_bad_donation():
    response = client.post(
        "/",
        json={
            "donor_name": "phil",
            "units_donated": "5",
            "donation_date": "2008-09-15"
        }
    )
    assert response.status_code == 422


def test_get_report():
    client.post(
        "/",
        json={
            "donor_name": "sasha",
            "donation_type": "clothes",
            "units_donated": "4",
            "donation_date": "2012-10-15"
        }
    )
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "donations": [
            {
                "donor_name": "sasha",
                "donation_type": "clothes",
                "units_donated": "4",
                "donation_date": "2012-10-15"
            }
        ]
    }

    teardown()
