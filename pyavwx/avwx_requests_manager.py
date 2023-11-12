import json

import requests

from pyavwx.avwx_authentication import AvwxApiAuth
from pyavwx.avwx_exceptions import AvwxBadStatus


def makeRequest(
    url: str,
    auth: AvwxApiAuth,
    data: str = None,
    rjson: bool = True,
    method: str = "GET",
) -> tuple:
    if method == "GET":
        r = requests.get(url=url, auth=auth, data=data)
    elif method == "POST":
        r = requests.post(url=url, auth=auth, data=data)
    else:
        raise AttributeError("Method incorrect : not 'POST' or 'GET'")
    if r.status_code != requests.codes.ok:
        raise AvwxBadStatus(request=r)
    if rjson:
        return r, json.loads(r.text)
    else:
        return (r,)
