import requests
import json


def test_entry_get():
    response = requests.get("http://localhost:5000/entry/1")

    assert response.status_code == 200

def test_entry_patch():

    example_post = {
        "title": "Habenero Sizzle",
        "description": "",
        "heat_level": "medium"
    }

    example_patch = {
        "title": "Habenero Sizzle",
        "description": "It's really hot!",
        "heat_level": "hot"
    }

    headers = {
        "Content-Type": "application/json"
    }

    post_response = requests.post("http://localhost:5000/entries", headers=headers, data=json.dumps(example_post))

    post_id = post_response.json()['id']
    response = requests.patch("http://localhost:5000/entry/{}".format(post_id), headers=headers, data=json.dumps(example_patch))

    assert response.status_code == 200

def test_entry_delete():
    example_post = {
        "title": "Thai Chili Express",
        "description": "Basil and Thai flavoured sauce",
        "heat_level": "medium"
    }

    headers = {
        "Content-Type": "application/json"
    }

    post_response = requests.post("http://localhost:5000/entries", headers=headers, data=json.dumps(example_post))

    post_id = post_response.json()['id']
    response = requests.delete("http://localhost:5000/entry/{}".format(post_id), headers=headers)

    assert response.status_code == 204