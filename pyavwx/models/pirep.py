import json
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
    station: str = None
    distance: Distance = None


@nested_dataclass
class Time:
    repr: int = None
    dt: datetime = None


@nested_dataclass
class Turbulance:
    severity: str = None
    floor: any = None
    ceiling: any = None


@nested_dataclass
class Datum:
    raw: str = None
    station: str = None
    time: Time = None
    aircraft: Aircraft = None
    altitude: Altitude = None
    clouds: list[Cloud] = None
    flight_visibility: any = None
    icing: any = None
    location: Location = None
    other: list[any] = None
    sanitized: str = None
    temperature: any = None
    turbulance: Turbulance = None
    type: str = None
    wx_codes: list[any] = None
    remarks: str = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)


@nested_dataclass
class Pirep:
    meta: Meta = None
    data: list[Datum] = None
    units: Units = None
    timestamp: datetime = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
