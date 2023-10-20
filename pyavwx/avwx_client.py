import json

import requests
from typing import Optional

from pyavwx.avwx_authentication import AvwxApiAuth
from pyavwx.const import BASE_URL
from pyavwx.models.metar import Metar
from pyavwx.avwx_exceptions import AvwxBadStatus


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
            onfial: str = None,
            url_modifier: str = "metar/") -> Metar:

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

        r = requests.get(url=url, auth=self.auth)
        if r.status_code != requests.codes.ok:
            raise AvwxBadStatus(request=r)
        r = json.loads(r.text)
        return Metar(**r)
