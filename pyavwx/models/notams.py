import json
from dataclasses import dataclass
from datetime import datetime

from pyavwx.models.structs import Meta, Time, TypeClass, Coord
from pyavwx.models.utils import nested_dataclass


@dataclass
class Lower:
    repr: str = None
    value: int = None
    spoken: str = None


@dataclass
class Upper:
    repr: int = None
    value: int = None
    spoken: str = None


@nested_dataclass
class Qualifiers:
    repr: str = None
    fir: str = None
    subject: TypeClass = None
    condition: TypeClass = None
    traffic: TypeClass = None
    purpose: list[TypeClass] = None
    scope: list[TypeClass] = None
    lower: Lower = None
    upper: Upper = None
    coord: Coord = None
    radius: Lower = None


@dataclass
class StartTime:
    repr: int = None
    dt: datetime = None


@nested_dataclass
class Datum:
    raw: str = None
    sanitized: str = None
    station: str = None
    time: Time = None
    remarks: str = None
    number: str = None
    replaces: None = None
    type: TypeClass = None
    qualifiers: Qualifiers = None
    start_time: StartTime = None
    end_time: Time = None
    schedule: any = None
    body: str = None
    lower: any = None
    upper: any = None


@nested_dataclass
class Notam:
    meta: Meta = None
    data: list[Datum] = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
