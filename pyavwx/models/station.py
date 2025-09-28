import json
from dataclasses import dataclass

from pyavwx.models.airSigmet import AirSigmet
from pyavwx.models.metar import Metar
from pyavwx.models.notams import Notam
from pyavwx.models.structs import Meta, Station
from pyavwx.models.taf import Taf
from pyavwx.models.utils import nested_dataclass


@nested_dataclass
class NearStation:
    station: Station = None
    coordinate_distance: float = None
    nautical_miles: float = None
    miles: float = None
    kilometers: float = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)


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

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)


@nested_dataclass
class ReportsRoute:
    meta: Meta = None
    route: list[Route] = None
    results: Metar | Taf | AirSigmet | Notam = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
