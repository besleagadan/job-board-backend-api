import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_candidate_register(api_client):
    url = reverse("register")
    data = {
        "username": "john",
        "email": "john@example.com",
        "password": "pass1234",
        # "role": "candidate"
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert response.data["username"] == "john"