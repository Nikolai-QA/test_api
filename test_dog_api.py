import requests
import pytest
from config import BASE_URL_DOG


def test_get_all_breeds():
    response = requests.get(f"{BASE_URL_DOG}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], dict)


def test_get_random_dog_image():
    response = requests.get(f"{BASE_URL_DOG}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"].startswith("https://images.dog.ceo/")


@pytest.mark.parametrize("breed", ["husky", "labrador", "beagle"])
def test_get_random_breed_image(breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert f"/{breed}/" in data["message"]


@pytest.mark.parametrize("invalid_breed", ["dragon", "unicorn", "robotdog"])
def test_get_invalid_breed(invalid_breed):
    response = requests.get(f"{BASE_URL_DOG}/breed/{invalid_breed}/images/random")
    assert response.status_code == 404  # API возвращает 404 на несуществующую породу
    data = response.json()
    assert data["status"] == "error"


def test_get_multiple_random_images():
    num_images = 3
    response = requests.get(f"{BASE_URL_DOG}/breeds/image/random/{num_images}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)
    assert len(data["message"]) == num_images
    assert all(img.startswith("https://images.dog.ceo/") for img in data["message"])