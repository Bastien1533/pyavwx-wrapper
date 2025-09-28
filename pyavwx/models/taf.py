import json
from dataclasses import dataclass
from typing import List, Any, Optional

from pyavwx.models.structs import (
    Cloud,
    Visibility,
    Wind,
    Time,
    Units,
    Meta,
    Station,
    Altimeter
)
from pyavwx.models.utils import nested_dataclass


@dataclass
class Probability:
    repr: str = None
    value: int = None
    spoken: str = None


@dataclass
class WxCode:
    repr: str = None
    value: str = None


@nested_dataclass
class Forecast:
    altimeter: Altimeter = None
    clouds: list[Cloud] = None
    flight_rules: str = None
    other: list[Any] = None
    sanitized: str = None
    visibility: Visibility = None
    wind_direction: Wind = None
    wind_speed: Wind = None
    wx_codes: list[WxCode] = None
    end_time: Time = None
    icing: list[Any] = None
    probability: Probability = None
    raw: str = None
    start_time: Time = None
    transition_start: Time = None
    turbulence: list[Any] = None
    type: str = None
    sanitized_type: str = None
    wind_variable_direction: Wind = None
    wind_shear: Wind = None
    summary: str = None
    wind_gust: Wind = None

    def __post_init__(self):
        self.sanitized_type = self.type.replace('BECMG', 'Becoming From').replace('FROM', 'From').replace('TEMPO',
                                                                                                          f'Temporary From {self.start_time.dt} to {self.end_time.dt}"')


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
    alts: any = None
    temps: any = None
    units: Units = None
    info: Station = None
    is_amended: bool = False
    is_correction: bool = False

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
