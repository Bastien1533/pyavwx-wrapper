import json
from typing import Any

from pyavwx.models.structs import (
    Altimeter,
    Cloud,
    Visibility,
    Wind,
    WxCode,
    Time,
    Dewpoint,
    RemarksInfo,
    RunwayVisibility,
    Units,
    Meta,
    Translate,
    Station,
)
from pyavwx.models.utils import nested_dataclass


@nested_dataclass
class Metar:
    meta: Meta = None
    altimeter: Altimeter = None
    clouds: list[Cloud] = None
    flight_rules: str = None
    other: list[Any] = None
    visibility: Visibility = None
    wind_direction: Wind = None
    wind_gust: Wind = None
    wind_speed: Wind = None
    wx_codes: list[WxCode] = None
    raw: str = None
    sanitized: str = None
    station: str = None
    time: Time = None
    remarks: str = None
    dewpoint: Dewpoint = None
    relative_humidity: float = None
    remarks_info: RemarksInfo = None
    runway_visibility: list[RunwayVisibility] = None
    temperature: Dewpoint = None
    wind_variable_direction: list[Any] = None
    density_altitude: int = None
    pressure_altitude: int = None
    units: Units = None
    summary: str = None
    speech: str = None
    translate: Translate = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
