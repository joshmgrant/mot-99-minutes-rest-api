import pytest


post_testdata = [{
        'title': "A Sauce",
        'description': 'Some kind of hot sauce',
        'heat_level': 'medium'
    },{
        'title': "Sauce with No Description",
        'description': '',
        'heat_level': 'mild'
    }, {
        'title': "Sauce with No Heat Level",
        'description': 'A pretty good sauce',
        'heat_level': ''
    }, {
        'title': "Sauce with Nothing",
        'description': '',
        'heat_level': ''
    }, {
        'title': "",
        'description': '',
        'heat_level': ''
}]

def test_entries_get(saucelog):
    response = saucelog.get("/entries")

    assert response.status_code_is(200)

@pytest.mark.parametrize("example_post", post_testdata)
def test_entries_post(saucelog, example_post):

    response = saucelog.post("/entries", data=example_post)

    assert response.status_code_is(200)