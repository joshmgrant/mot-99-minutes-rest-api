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
        return response

    def get(self, endpoint):
        """Basic GET request."""        
        response = requests.get(
            "{}{}".format(self.base_url, endpoint),
            headers=self.headers
        )
        return response

    def delete(self, endpoint):
        """Basic DELETE request."""
        response = requests.delete(
            "{}{}".format(self.base_url, endpoint),
            headers=self.headers
        )
        return response

    def patch(self, endpoint, data):
        """Basic PATCH request."""
        response = requests.patch(
            "{}{}".format(self.base_url, endpoint),
            data=json.dumps(data),
            headers=self.headers
        )
        return response