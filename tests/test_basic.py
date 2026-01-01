import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_200():
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
    assert len(r.json()) > 0


