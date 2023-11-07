from dataclasses import dataclass

from pyavwx.models.structs import Meta, Station
from pyavwx.models.utils import nested_dataclass


@nested_dataclass
class NearStation:
    station: Station = None
    coordinate_distance: float = None
    nautical_miles: float = None
    miles: float = None
    kilometers: float = None


@dataclass
class Route:
    lat: float = None
    lon: float = None
    repr: str = None


@nested_dataclass
class StationRoute:
    meta: Meta = None
    route: list[Route] = None
    results: list[Station] = None
