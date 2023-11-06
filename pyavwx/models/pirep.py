import json
from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime

from pyavwx.models.structs import Distance, Altitude, Units, Meta, Station, Cloud
from pyavwx.models.utils import nested_dataclass


@nested_dataclass
class Aircraft:
    code: str = None
    type: str = None


@nested_dataclass
class Location:
    repr: str = None
    station: Optional[str] = None
    distance: Optional[Distance] = None


@nested_dataclass
class Time:
    repr: int = None
    dt: datetime = None


@nested_dataclass
class Turbulance:
    severity: str = None
    floor: Any = None
    ceiling: Any = None


@nested_dataclass
class Datum:
    raw: str = None
    station: str = None
    time: Time = None
    aircraft: Aircraft = None
    altitude: Altitude = None
    clouds: list[Cloud] = None
    flight_visibility: Any = None
    icing: Any = None
    location: Location = None
    other: list[Any] = None
    sanitized: str = None
    temperature: Any = None
    turbulance: Turbulance = None
    type: str = None
    wx_codes: list[Any] = None
    remarks: Optional[str] = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)


@nested_dataclass
class Pirep:
    meta: Meta = None
    data: list[Datum] = None
    units: Units = None
    timestamp: datetime = None
    
    
    