from ..conftest import client

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