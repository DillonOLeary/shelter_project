from ..conftest import client, generate_database


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
