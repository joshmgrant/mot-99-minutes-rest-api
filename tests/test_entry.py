def test_entry_get(saucelog):
    response = (saucelog.get("/entry/1"))

    assert response.status_code_is(200)

def test_entry_patch(saucelog):

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

    post_response = saucelog.post("/entries", data=example_post)

    post_id = post_response['id']
    response = saucelog.patch("/entry/{}".format(post_id), data=example_patch)

    assert response.status_code_is(200)

def test_entry_delete(saucelog):
    example_post = {
        "title": "Thai Chili Express",
        "description": "Basil and Thai flavoured sauce",
        "heat_level": "medium"
    }

    post_response = saucelog.post("/entries", data=example_post)

    post_id = post_response['id']
    response = saucelog.delete("/entry/{}".format(post_id))

    assert response.status_code_is(204)