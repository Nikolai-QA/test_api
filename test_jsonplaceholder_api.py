import requests
import pytest
from config import BASE_URL_JSONPLACEHOLDER

def test_get_all_users():
    response = requests.get(f"{BASE_URL_JSONPLACEHOLDER}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_user_by_id():
    user_id = 1
    response = requests.get(f"{BASE_URL_JSONPLACEHOLDER}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["id"] == user_id

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(user_id):
    response = requests.get(f"{BASE_URL_JSONPLACEHOLDER}/posts", params={"userId": user_id})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for post in data:
        assert post["userId"] == user_id

@pytest.mark.parametrize("title, body", [("New Post", "This is a new post"), ("Test Post", "Test body")])
def test_create_post(title, body):
    new_post = {
        "title": title,
        "body": body,
        "userId": 1
    }
    response = requests.post(f"{BASE_URL_JSONPLACEHOLDER}/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == title
    assert data["body"] == body
    assert data["userId"] == 1

def test_get_comments_by_post():
    post_id = 1
    response = requests.get(f"{BASE_URL_JSONPLACEHOLDER}/comments", params={"postId": post_id})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for comment in data:
        assert comment["postId"] == post_id
