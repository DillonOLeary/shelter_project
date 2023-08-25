from .conftest import client, generate_database

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


def test_get_balances():
    generate_database()
    response = client.get("/balances/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "category": "money",
            "quantity": 11.0
        },
        {
            "category": "clothes",
            "quantity": 2.0
        }
    ]


def test_get_donor_records():
    generate_database()
    response = client.get("/donor-records/")
    assert response.status_code == 200
    assert response.json() == [
        {
            "donor": "phil",
            "record": [
                {
                    "category": "money",
                    "quantity": 12.0
                },
                {
                    "category": "clothes",
                    "quantity": 2.0
                }
            ]
        },
        {
            "donor": "kristin",
            "record": [
                {
                    "category": "money",
                    "quantity": 3.0
                }
            ]
        }
    ]
