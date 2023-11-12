import avwx
import pytest
from dataclasses import asdict

import pyavwx


def cast_metar(icao):
    try:
        avwx_metar = avwx.Metar(icao)
        avwx_metar.update()
        return pyavwx.models.Metar(**asdict(avwx_metar.data))
    except Exception as e:
        pytest.fail(e)


def cast_taf(icao):
    try:
        avwx_taf = avwx.Taf(icao)
        avwx_taf.update()
        return pyavwx.models.Taf(**asdict(avwx_taf.data))
    except Exception as e:
        pytest.fail(e)


def cast_station(icao):
    try:
        avwx_taf = avwx.station.search(icao, limit=1)
        return pyavwx.models.Station(**asdict(avwx_taf[0]))
    except Exception as e:
        pytest.fail(e)


def test_metar():
    assert type(cast_metar("LFPG")) == pyavwx.models.Metar


def test_taf():
    assert type(cast_taf("LFPG")) == pyavwx.models.Taf


def test_station():
    assert type(cast_station("LFPG")) == pyavwx.models.Station
