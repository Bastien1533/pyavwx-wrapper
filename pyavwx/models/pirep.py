import json
from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime

from pyavwx.models.structs import (
    Distance,
    Altitude,
    Units,
    Meta,
    Info
)
from pyavwx.models.utils import nested_dataclass



@nested_dataclass
class Aircraft:
    code: str
    type: str


@nested_dataclass
class Location:
    repr: str
    station: Optional[str] = None
    distance: Optional[Distance] = None


@nested_dataclass
class Time:
    repr: int
    dt: datetime


@nested_dataclass
class Turbulance:
    severity: str
    floor: None
    ceiling: None


@nested_dataclass
class Datum:
    raw: str
    station: str
    time: Time
    aircraft: Aircraft
    altitude: Altitude
    clouds: None
    flight_visibility: None
    icing: None
    location: Location
    other: List[Any]
    sanitized: str
    temperature: None
    turbulance: Turbulance
    type: str
    wx_codes: List[Any]
    remarks: Optional[str] = None
    info: Info = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)


@nested_dataclass
class Pirep:
    meta: Meta
    data: List[Datum]
    units: Units
    timestamp: datetime
