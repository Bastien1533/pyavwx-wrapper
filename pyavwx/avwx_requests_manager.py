import requests
import json

from pyavwx.avwx_exceptions import AvwxBadStatus
from pyavwx.avwx_authentication import AvwxApiAuth


def makeRequest(url: str, auth: AvwxApiAuth, rjson: bool) -> tuple:
    r = requests.get(url=url, auth=auth)
    if r.status_code != requests.codes.ok:
        raise AvwxBadStatus(request=r)
    if rjson:
        return r, json.loads(r.text)
    else:
        return r, 
