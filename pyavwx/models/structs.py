import json
from dataclasses import dataclass
from datetime import datetime

from pyavwx.models.utils import nested_dataclass


@dataclass
class Coord:
    lat: float = None
    lon: float = None
    repr: str = None


@dataclass
class TypeClass:
    repr: str = None
    value: str = None


@dataclass
class Ceiling:
    altitude: int = None
    modifier: dict = None
    repr: str = None
    type: str = None


@dataclass
class Code:
    repr: str = None
    value: str = None


@dataclass
class Precip36_Hours:
    repr: int = None
    value: float = None
    spoken: str = None


@dataclass
class PressureTendency:
    repr: int = None
    tendency: str = None
    change: float = None


@dataclass
class Altimeter:
    repr: str = None
    value: float = None
    spoken: str = None


@dataclass
class Altitude:
    repr: int = None
    value: int = None
    spoken: str = None


@dataclass
class DecimalRepr:
    repr: str = None
    value: float = None
    spoken: str = None


@dataclass
class Cloud:
    repr: str = None
    type: str = None
    base: int = None
    top: any = None
    altitude: int = None
    modifier: DecimalRepr = None
    direction: any = None


@dataclass
class Dewpoint:
    repr: str = None
    value: int = None
    spoken: str = None


@dataclass
class Distance:
    repr: str = None
    value: int = None
    spoken: str = None


@dataclass
class Meta:
    timestamp: datetime = None
    stations_updated: datetime = None
    cache_timestamp: datetime = None


@dataclass
class WxCode:
    repr: str = None
    value: str = None


@nested_dataclass
class RemarksInfo:
    maximum_temperature_6: DecimalRepr = None
    minimum_temperature_6: DecimalRepr = None
    pressure_tendency: DecimalRepr = None
    precip_36__hours: DecimalRepr = None
    precip_24__hours: DecimalRepr = None
    sunshine_minutes: DecimalRepr = None
    codes: list[WxCode] = None
    dewpoint_decimal: DecimalRepr = None
    maximum_temperature_24: DecimalRepr = None
    minimum_temperature_24: DecimalRepr = None
    precip_hourly: DecimalRepr = None
    sea_level_pressure: Altimeter = None
    snow_depth: DecimalRepr = None
    temperature_decimal: DecimalRepr = None


@dataclass
class Wind:
    repr: int = None
    value: int = None
    spoken: str = None


@nested_dataclass
class RunwayVisibility:
    repr: str = None
    runway: int = None
    visibility: DecimalRepr = None
    variable_visibility: list[Wind] = None
    trend: WxCode = None


@nested_dataclass
class Time:
    repr: str = None
    dt: datetime = None


@dataclass
class Units:
    accumulation: str = None
    altimeter: str = None
    altitude: str = None
    temperature: str = None
    visibility: str = None
    wind_speed: str = None


@dataclass
class Visibility:
    repr: str = None
    value: float = None
    spoken: str = None
    numerator: int = None
    denominator: int = None
    normalized: str = None


@dataclass
class Remarks:
    slp091: str = None


@dataclass
class Translate:
    altimeter: str = None
    clouds: str = None
    wx_codes: str = None
    visibility: str = None
    dewpoint: str = None
    remarks: Remarks = None
    temperature: str = None
    wind: str = None


@dataclass
class Local:
    pass


@dataclass
class Runway:
    length_ft: int = None
    width_ft: int = None
    surface: str = None
    lights: bool = None
    ident1: str = None
    ident2: str = None
    bearing1: int = None
    bearing2: int = None


@nested_dataclass
class Station:
    city: str = None
    country: str = None
    elevation_ft: int = None
    elevation_m: int = None
    gps: str = None
    iata: str = None
    icao: str = None
    latitude: float = None
    local: str = None
    longitude: float = None
    name: str = None
    note: str = None
    reporting: bool = None
    runways: list[Runway] = None
    state: str = None
    type: str = None
    website: str = None
    wiki: str = None
    coordinate_distance: float = None
    nautical_miles: float = None
    miles: float = None
    kilometers: float = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
