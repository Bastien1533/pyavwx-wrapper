from dataclasses import dataclass
from typing import Any

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
    start_time: Any = None
    end_time: Any = None
    position: Any = None
    floor: Ceiling = None
    ceiling: Ceiling = None
    coords: list[Coord] = None
    bounds: list[Any] = None
    movement: Any = None
    intensity: Any = None
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
    correction: Any = None
    area: str = None
    type: str = None
    start_time: Time = None
    end_time: Time = None
    body: str = None
    region: str = None
    observation: Observation = None
    forecast: Any = None
    units: Units = None


@dataclass
class AirSigmet:
    meta: Meta = None
    reports: list[Report] = None
