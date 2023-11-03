import json

from typing import Optional

from pyavwx.avwx_authentication import AvwxApiAuth
from pyavwx.const import BASE_URL
from pyavwx.models.metar import Metar
from pyavwx.avwx_exceptions import AvwxBadStatus
from pyavwx.avwx_requests_manager import makeRequest


class AvwxApiClient:
    def __init__(self, api_key):
        self.auth = AvwxApiAuth(api_key)

    def url_builder(self, url_modifier: str, base_url: str, args: dict, main_payload: str) -> str:

        url = base_url + url_modifier + f"{args[main_payload]}?"
        if args.get("self"):
            del args["self"]
        if args.get("url_modifier"):
            del args["url_modifier"]

        for arg in args:
            value = args.get(arg)
            if value:
                url = url + f'{arg}={str(value).replace(" ", "")}&'
        return url

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

        # Building URL: 
        # To get something like that: metar?options=translate&format=json&remove=&filter=
        # We directly take the function args if they are provided, without self and url_modifier
        args = locals()
        url = ""
        print(url)
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

        # Building URL: 
        # To get something like that: metar?options=translate&format=json&remove=&filter=
        # We directly take the function args if they are provided, without self and url_modifier
        args = locals()

        url = BASE_URL + url_modifier + f"{args['location']}?"
        if args.get("self"):
            del args["self"]
        if args.get("url_modifier"):
            del args["url_modifier"]

        for arg in args:
            value = args.get(arg)
            if value:
                url = url + f'{arg}={str(value).replace(" ", "")}&'

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object. 
        r = makeRequest(url=url, auth=self.auth, rjson=True)[1]
        return Metar(**r)
