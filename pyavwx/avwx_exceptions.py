import json
import requests

from pyavwx.models.exceptions import StationError, AuthError
from pyavwx.models.metar import Metar


class AvwxBadStatus(Exception):
    def __init__(self, request: requests.Response):
        self.status = request.status_code
        if request.status_code == 400:
            self.exception = StationError(**json.loads(request.text))

        if request.status_code == 401:
            self.exception = AuthError(**(json.loads(request.text)))
        self.args = (self.status, self.exception, Metar(**self.exception.sample))

    def __str__(self):
        return f"[Status_Code:{self.status}] {self.exception.error}"
