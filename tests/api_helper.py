import requests
import json


class API(object):
    """API Wrapper
    Similar approach as with the Page Object pattern."""

    def __init__(self, base_url=None):
        self.headers = {"Content-Type": "application/json"}
        self.base_url = base_url if base_url else 'http://localhost:5000/'

    def post(self, endpoint, data):
        """Basic POST request."""
        response = requests.post(
            "{}{}".format(self.base_url, endpoint),
            data=json.dumps(data),
            headers=self.headers
        )
        return APIResponse(response=response)

    def get(self, endpoint):
        """Basic GET request."""        
        response = requests.get(
            "{}{}".format(self.base_url, endpoint),
            headers=self.headers
        )
        return APIResponse(response=response)

    def delete(self, endpoint):
        """Basic DELETE request."""
        response = requests.delete(
            "{}{}".format(self.base_url, endpoint),
            headers=self.headers
        )
        return APIResponse(response=response)

    def patch(self, endpoint, data):
        """Basic PATCH request."""
        response = requests.patch(
            "{}{}".format(self.base_url, endpoint),
            data=json.dumps(data),
            headers=self.headers
        )
        return APIResponse(response=response)
    
class APIResponse(dict):
    def __init__(self, response):
        """Initalizer for APIResponse.
        Parse a request response into a dict format.
        Also handle custom response behaviours via the
        custom_response() method.
        """
        self._response = response
        self['status_code'] = response.status_code
        self._custom_response(response)

    def __getitem__(self, key):
        """Override __getitme__.
        
        This replaces the KeyError behaviour with a ('unknown key', None)
        pattern which is better suited to many test automation contexts.
        """
        try:
            return super().__getitem__(key)
        except KeyError:
            super().__setitem__(key, None)

        return super().__getitem__(key)

    def _custom_response(self, response):
        """Handle custom response behaviours.""" 
        try:
            if type(response.json()) == list:
                super().__init__({'list': response.json()})
            else:
                super().__init__(response.json())
        except json.decoder.JSONDecodeError as err:
            super().__init__({})

    
    def status_code_is(self, expected):
        return self['status_code'] == expected