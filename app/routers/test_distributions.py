from ..conftest import client

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