import json
from dataclasses import dataclass

from pyavwx.models.structs import (
    Units,
    Meta,
    Remarks,
    Station,
    Ceiling,
    Cloud,
    Time,
    Visibility,
)
from pyavwx.models.utils import nested_dataclass


@dataclass
class DataRepr:
    repr: int = None
    value: int = None
    spoken: str = None


@dataclass
class PrecipAmount6:
    repr: int = None
    value: float = None
    spoken: str = None


@dataclass
class PrecipType:
    repr: str
    value: str


@nested_dataclass
class Forecast:
    time: Time = None
    temperature: DataRepr = None
    dewpoint: DataRepr = None
    sky_cover: DataRepr = None
    vis_obstruction: Visibility = None
    visibility: Visibility = None
    wind_direction: DataRepr = None
    wind_speed: DataRepr = None
    wind_gust: DataRepr = None
    snow_level: DataRepr = None
    precip_duration: DataRepr = None
    freezing_precip: DataRepr = None
    snow: DataRepr = None
    sleet: DataRepr = None
    rain: DataRepr = None
    solar_radiation: DataRepr = None
    wave_height: DataRepr = None
    ceiling: Ceiling = None
    cloud_base: DataRepr = None
    cloud: Cloud = None
    precip_type: PrecipType = None
    mixing_height: DataRepr = None
    transport_wind_direction: DataRepr = None
    transport_wind_speed: DataRepr = None
    precip_chance_12: DataRepr = None
    precip_amount_12: DataRepr = None
    thunderstorm_12: DataRepr = None
    thunderstorm_3: DataRepr = None
    thunderstorm_1: DataRepr = None
    thunder_storm_12: DataRepr = None
    thunder_storm_6: DataRepr = None
    haines: DataRepr = None
    precip_chance_6: DataRepr = None
    precip_chance_1: DataRepr = None
    precip_amount_6: PrecipAmount6 = None
    precip_amount_1: DataRepr = None
    snow_amount_6: DataRepr = None
    snow_amount_1: DataRepr = None
    icing_amount_6: DataRepr = None
    icing_amount_1: DataRepr = None
    severe_storm_12: DataRepr = None
    severe_storm_6: DataRepr = None
    severe_storm_3: DataRepr = None
    severe_storm_1: DataRepr = None


@nested_dataclass
class Nbm:
    meta: Meta = None
    raw: str = None
    station: str = None
    time: Time = None
    remarks: any = None
    forecast: list[Forecast] = None
    units: Units = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)


@nested_dataclass
class Gfs:
    meta: Meta = None
    raw: str = None
    station: str = None
    time: Time = None
    remarks: list[Remarks] = None
    forecast: list[Forecast] = None
    units: Units = None
    info: Station = None

    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__, default=lambda k: k.__dict__)
