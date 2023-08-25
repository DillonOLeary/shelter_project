from ..conftest import client


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
