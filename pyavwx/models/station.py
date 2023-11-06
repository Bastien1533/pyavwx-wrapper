import json
from datetime import datetime

from pyavwx.models.structs import Distance, Altitude, Units, Meta, Station, Cloud
from pyavwx.models.utils import nested_dataclass

from dataclasses import  dataclass





@nested_dataclass
class NearStation:
    station: Station = None
    coordinate_distance: float = None
    nautical_miles: float = None
    miles: float = None
    kilometers: float = None
