import json
from dataclasses import dataclass

from pyavwx.models.structs import Units, Meta, Time, Remarks, Station, TypeClass, Coord


@dataclass
class Bulletin:
    repr: str = None
    type: TypeClass = None
    country: str = None
    number: int = None


@dataclass
class Ceiling:
    repr: str = None
    value: int = None
    spoken: str = None


@dataclass
class Observation:
    type: TypeClass = None
    start_time: any = None
    end_time: any = None
    position: any = None
    floor: Ceiling = None
    ceiling: Ceiling = None
    coords: list[Coord] = None
    bounds: list[any] = None
    movement: any = None
    intensity: any = None
    other: list[str] = None


@dataclass
class Report:
    raw: str = None
    sanitized: str = None
    station: Station = None
    time: Time = None
    remarks: Remarks = None
    bulletin: Bulletin = None
    issuer: str = None
    correction: any = None
    area: str = None
    type: str = None
    start_time: Time = None
    end_time: Time = None
    body: str = None
    region: str = None
    observation: Observation = None
    forecast: any = None
    units: Units = None


@dataclass
class AirSigmet:
    meta: Meta = None
    reports: list[Report] = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
