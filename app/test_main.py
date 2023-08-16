from fastapi.testclient import TestClient
from .main import app

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
        "donation_date": "2008-09-15",
        "timestamp": "12345"
    }

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
