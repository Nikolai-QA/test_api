import requests
import pytest
from config import BASE_URL_BREWERY

def test_get_all_breweries():
    response = requests.get(f"{BASE_URL_BREWERY}/breweries")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

@pytest.mark.parametrize("city", ["New York", "Los Angeles", "Chicago"])
def test_get_breweries_by_city(city):
    response = requests.get(f"{BASE_URL_BREWERY}/breweries", params={"by_city": city})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        for brewery in data:
            assert "city" in brewery
            assert city.lower() in brewery["city"].lower()

def test_get_brewery_by_id():
    brewery_id = "5128df48-79fc-4f0f-8b52-d06be54d0cec"
    response = requests.get(f"{BASE_URL_BREWERY}/breweries/{brewery_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == brewery_id

@pytest.mark.parametrize("brewery_type", ["micro", "regional", "brewpub"])
def test_get_breweries_by_type(brewery_type):
    response = requests.get(f"{BASE_URL_BREWERY}/breweries", params={"by_type": brewery_type})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        for brewery in data:
            assert "brewery_type" in brewery
            assert brewery["brewery_type"] == brewery_type

def test_get_invalid_brewery():
    invalid_id = "non-existent-brewery"
    response = requests.get(f"{BASE_URL_BREWERY}/breweries/{invalid_id}")
    assert response.status_code == 404


