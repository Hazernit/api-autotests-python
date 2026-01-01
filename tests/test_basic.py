import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_200_and_list():
    r = requests.get(f"{BASE_URL}/posts")
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_post_1_has_expected_fields():
    r = requests.get(f"{BASE_URL}/posts/1")
    assert r.status_code == 200

    post = r.json()
    assert post["id"] == 1
    assert "title" in post and isinstance(post["title"], str)
    assert "body" in post and isinstance(post["body"], str)


def test_get_nonexistent_post_returns_empty_or_404():
    r = requests.get(f"{BASE_URL}/posts/999999")

    # jsonplaceholder обычно возвращает 200 и пустой объект {}
    assert r.status_code in (200, 404)

    if r.status_code == 200:
        assert r.json() in ({}, [])
