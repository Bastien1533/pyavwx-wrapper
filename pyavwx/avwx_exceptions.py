import json
import requests

from pyavwx.models.exceptions import StationError


class AvwxBadStatus(Exception):
    def __init__(self, request: requests.Response):
        if request.status_code == 400:
            self.exception = StationError(**json.loads(request.text))

    def get_exception(self):
        return self.exception
