import json

from typing import Optional

from pyavwx.avwx_authentication import AvwxApiAuth
from pyavwx.models.utils import url_builder
from pyavwx.models import Metar, Taf
from pyavwx.avwx_requests_manager import makeRequest
from pyavwx.const import BASE_URL


class AvwxApiClient:
    def __init__(self, api_key):
        self.auth = AvwxApiAuth(api_key)

    def get_metar(
            self,
            location: str,
            options: str = None,
            airport: bool = None,
            reporting: bool = None,
            remove: str = None,
            filter: str = None,
            onfail: str = None,
            url_modifier: str = "metar/") -> Metar:

        args = locals()
        url = url_builder(url_modifier=url_modifier, base_url=BASE_URL, main_payload=args['location'], args=args)

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object. 
        r = makeRequest(url=url, auth=self.auth, rjson=True)[1]
        return Metar(**r)

    def parse_metar(
            self,
            metar,
            options,
            remove,
            filter,
            url_modifier: str = "parse/metar/") -> Metar:

        args = locals()
        url = url_builder(url_modifier=url_modifier, base_url=BASE_URL, main_payload=metar, args=args)

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object. 
        r = makeRequest(url=url, auth=self.auth, rjson=True)[1]
        return Metar(**r)

    def get_taf(
                self,
                location: str,
                options: str = None,
                airport: bool = None,
                reporting: bool = None,
                remove: str = None,
                filter: str = None,
                onfail: str = None,
                url_modifier: str = "taf/") -> Taf:

        args = locals()
        url = url_builder(url_modifier=url_modifier, base_url=BASE_URL, main_payload=args['location'], args=args)

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object. 
        r = makeRequest(url=url, auth=self.auth, rjson=True)[1]
        return Taf(**r)
