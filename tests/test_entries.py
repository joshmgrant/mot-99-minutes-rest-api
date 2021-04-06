import requests
import json

def test_entries_get():
    response = requests.get("http://localhost:5000/entries")

    assert response.status_code == 200

def test_entries_post():
    example_post = {
        'title': "A Sauce",
        'description': 'Some kind of hot sauce',
        'heat_level': 'medium'
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post("http://localhost:5000/entries", headers=headers, data=json.dumps(example_post))

    assert response.status_code == 200