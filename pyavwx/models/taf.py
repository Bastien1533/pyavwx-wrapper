import json
from typing import List, Any, Optional

from pyavwx.models.structs import (
    Cloud,
    Visibility,
    Wind,
    Time,
    Units,
    Meta,
    Station,
)
from pyavwx.models.utils import nested_dataclass


@nested_dataclass
class Probability:
    repr: str = None
    value: int = None
    spoken: str = None


@nested_dataclass
class WxCode:
    repr: str = None
    value: str = None


@nested_dataclass
class Forecast:
    altimeter: str = None
    clouds: List[Cloud] = None
    flight_rules: str = None
    other: List[Any] = None
    sanitized: str = None
    visibility: Visibility = None
    wind_direction: Wind = None
    wind_speed: Wind = None
    wx_codes: List[WxCode] = None
    end_time: Time = None
    icing: List[Any] = None
    probability: Probability = None
    raw: str = None
    start_time: Time = None
    transition_start: Time = None
    turbulence: List[Any] = None
    type: str = None
    wind_variable_direction: Wind = None
    wind_shear: Wind = None
    summary: str = None
    wind_gust: Optional[Wind] = None


@nested_dataclass
class Taf:
    meta: Meta = None
    raw: str = None
    station: str = None
    time: Time = None
    remarks: str = None
    remarks_info: dict = None
    forecast: List[Forecast] = None
    sanitized: str = None
    start_time: Time = None
    end_time: Time = None
    max_temp: str = None
    min_temp: str = None
    alts: str = None
    temps: str = None
    units: Units = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)
