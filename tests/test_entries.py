def test_entries_get(saucelog):
    response = saucelog.get("/entries")

    assert response.status_code_is(200)

def test_entries_post(saucelog):
    example_post = {
        'title': "A Sauce",
        'description': 'Some kind of hot sauce',
        'heat_level': 'medium'
    }

    response = saucelog.post("/entries", data=example_post)

    assert response.status_code_is(200)