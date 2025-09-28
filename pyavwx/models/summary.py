import json
from datetime import datetime

from pyavwx.models.metar import Translate
from pyavwx.models.structs import Meta, Station, Visibility, Ceiling
from pyavwx.models.utils import nested_dataclass


@nested_dataclass
class Metar:
    ceiling: Ceiling = None
    flight_rules: str = None
    time: datetime = None
    visibility: Visibility = None
    wx_codes: list[any] = None


@nested_dataclass
class Forecast:
    end_time: datetime = None
    flight_rules: str = None
    start_time: datetime = None


@nested_dataclass
class Taf:
    forecast: list[Forecast] = None
    time: datetime = None


@nested_dataclass
class Summary:
    meta: Meta = None
    metar: Metar = None
    taf: Taf = None
    summary: str = None
    speech: str = None
    translate: Translate = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
