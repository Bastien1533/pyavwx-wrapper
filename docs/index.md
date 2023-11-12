# Welcome to PyAvwx Wrapper 

## Why this library?
This wrapper has a 100% coverage of the [avwx.rest](https://avwx.rest) api.
It was created to have a seamless integration of this service in python. 
To check out the AVWX API specifications you can check [The Apiary Docs](https://avwx.docs.apiary.io/)


## Installation

PyAvwx is available via `pip`. You can install it with this command:

`pip install -U pyavwx-wrapper`

## Authentication

AVWX API uses api keys to function. If you don't have one you will need to create one in he [Accounts page](https://account.avwx.rest/)

```python
import pyavwx

api = pyavwx.AvwxApiClient("your-api-key")
```

The `api` variable will now hold the object `AvwxApiClient` that contains you api key. 

## Example : Requesting a Metar 
We will request a metar for LFPG.
We are using the api variable defined in Authentication
```python
metar = api.get_metar(location="LFPG")
print(metar)
'''Metar(
    meta=Meta(
        timestamp="2023-11-12T10:18:37.229481Z",
        stations_updated="2023-10-28",
        cache_timestamp=None,
    ),
    altimeter=Altimeter(repr="Q1004", value=1004, spoken="one zero zero four"),
    clouds=[
        Cloud(
            repr="BKN003",
            type="BKN",
            base=None,
            top=None,
            altitude=3,
            modifier=None,
            direction=None,
        ),
        Cloud(
            repr="BKN004",
            type="BKN",
            base=None,
            top=None,
            altitude=4,
            modifier=None,
            direction=None,
        ),
    ],
    flight_rules="LIFR",
    other=[],
    visibility=Visibility(
        repr="6000",
        value=6000,
        spoken="six thousand",
        numerator=None,
        denominator=None,
        normalized=None,
    ),
    wind_direction=Wind(repr="140", value=140, spoken="one four zero"),
    wind_gust=None,
    wind_speed=Wind(repr="11", value=11, spoken="one one"),
    wx_codes=[WxCode(repr="-DZ", value="Light Drizzle")],
    raw="LFPG 121000Z 14011KT 6000 -DZ BKN003 BKN004 07/07 Q1004 TEMPO 3000 DZ OVC002",
    sanitized="LFPG 121000Z 14011KT 6000 -DZ BKN003 BKN004 07/07 Q1004 TEMPO 3000 DZ OVC002",
    station="LFPG",
    time=Time(repr="121000Z", dt="2023-11-12T10:00:00Z"),
    remarks="TEMPO 3000 DZ OVC002",
    dewpoint=Dewpoint(repr="07", value=7, spoken="seven"),
    relative_humidity=1.0,
    remarks_info=RemarksInfo(
        maximum_temperature_6=None,
        minimum_temperature_6=None,
        pressure_tendency=None,
        precip_36__hours=None,
        precip_24__hours=None,
        sunshine_minutes=None,
        codes=[],
        dewpoint_decimal=None,
        maximum_temperature_24=None,
        minimum_temperature_24=None,
        precip_hourly=None,
        sea_level_pressure=None,
        snow_depth=None,
        temperature_decimal=None,
    ),
    runway_visibility=[],
    temperature=Dewpoint(repr="07", value=7, spoken="seven"),
    wind_variable_direction=[],
    density_altitude=-202,
    pressure_altitude=664,
    units=Units(
        accumulation="in",
        altimeter="hPa",
        altitude="ft",
        temperature="C",
        visibility="m",
        wind_speed="kt",
    ),
    summary=None,
    speech=None,
    translate=None,
    info=None)'''

```
