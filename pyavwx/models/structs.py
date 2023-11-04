from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime

from pyavwx.models.utils import nested_dataclass


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
class DewpointDecimal:
    pass


@dataclass
class Cloud:
    repr: str = None
    type: str = None
    altitude: int = None
    modifier: DewpointDecimal = None


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
    maximum_temperature_6: DewpointDecimal = None
    minimum_temperature_6: DewpointDecimal = None
    pressure_tendency: DewpointDecimal = None
    precip_36__hours: DewpointDecimal = None
    precip_24__hours: DewpointDecimal = None
    sunshine_minutes: DewpointDecimal = None
    codes: List[WxCode] = None
    dewpoint_decimal: DewpointDecimal = None
    maximum_temperature_24: DewpointDecimal = None
    minimum_temperature_24: DewpointDecimal = None
    precip_hourly: DewpointDecimal = None
    sea_level_pressure: Altimeter = None
    snow_depth: DewpointDecimal = None
    temperature_decimal: DewpointDecimal = None


@dataclass
class Wind:
    repr: int = None
    value: int = None
    spoken: str = None


@nested_dataclass
class RunwayVisibility:
    repr: str = None
    runway: int = None
    visibility: DewpointDecimal = None
    variable_visibility: List[Wind] = None
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
class Info:
    city: str = None
    country: str = None
    elevation_ft: int = None
    elevation_m: int = None
    gps: str = None
    iata: str = None
    icao: str = None
    latitude: float = None
    local: Local = None
    longitude: float = None
    name: str = None
    note: Local = None
    reporting: bool = None
    runways: List[Runway] = None
    state: str = None
    type: str = None
    website: Local = None
    wiki: str = None
