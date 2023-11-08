from pyavwx.avwx_authentication import AvwxApiAuth
from pyavwx.avwx_requests_manager import makeRequest
from pyavwx.const import BASE_URL
from pyavwx.models import (
    Metar,
    Taf,
    Pirep,
    Station,
    NearStation,
    StationRoute,
    Summary,
    AirSigmet,
    Notam,
    Nbm,
    Gfs
)
from pyavwx.models.utils import url_builder


class AvwxApiClient:
    def __init__(self, api_key):
        self.auth = AvwxApiAuth(api_key)

    def get_station(
        self,
        ident: str,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "station/",
    ) -> Station:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=args["ident"],
            args=args,
        )

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Station(**r[1])

    def get_near_stations(
        self,
        coords: str,
        n: int = 10,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "station/near/",
    ) -> list[NearStation]:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=args["coords"],
            args=args,
        )

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)

        station_list = []
        for station in r[1]:
            station_list.append(NearStation(**station))
        return station_list

    def get_stations_text(
        self,
        text: str,
        n: str = "10",
        remove: str = None,
        filter: str = None,
        url_modifier: str = "search/station",
    ) -> list[Station]:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload="",
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)

        station_list = []
        for station in r[1]:
            station_list.append(Station(**station))
        return station_list

    def get_stations_route(
        self,
        route: str,
        distance: int,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "path/station",
    ) -> StationRoute:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload="",
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)

        return StationRoute(**r[1])

    def get_summary(
        self,
        location: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "summary/",
    ) -> Summary:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=args["location"],
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Summary(**r[1])

    def get_metar(
        self,
        location: str,
        options: str = None,
        airport: bool = None,
        reporting: bool = None,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "metar/",
    ) -> Metar:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=args["location"],
            args=args,
        )

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Metar(**r[1])

    def parse_metar(
        self,
        metar: str = None,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/metar",
    ) -> Metar:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=metar,
            include_main=False,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True, data=metar, method="POST")
        return Metar(**r[1])

    def get_taf(
        self,
        location: str,
        options: str = None,
        airport: bool = None,
        reporting: bool = None,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "taf/",
    ) -> Taf:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=args["location"],
            args=args,
        )
        print(url)

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Taf(**r[1])

    def parse_taf(
        self,
        taf: str = None,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/taf",
    ) -> Taf:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=taf,
            include_main=False,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True, data=taf, method="POST")
        return Taf(**r[1])

    def get_pirep(
        self,
        location: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "pirep/",
    ) -> Pirep:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=args["location"],
            args=args,
        )

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Pirep(**r[1])

    def parse_pirep(
        self,
        pirep: str = None,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/pirep",
    ) -> Pirep:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=pirep,
            include_main=False,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True, data=pirep, method="POST")
        return Pirep(**r[1])

    def get_airsigmet(
        self,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "airsigmet",
    ) -> AirSigmet:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload="",
            args=args,
        )

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return AirSigmet(**r[1])

    def parse_airsigmet(
        self,
        airsigmet: str = None,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/airsigmet",
    ) -> AirSigmet:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=airsigmet,
            include_main=False,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(
            url=url, auth=self.auth, rjson=True, data=airsigmet, method="POST"
        )
        return AirSigmet(**r[1])

    def get_notam(
        self,
        location: str,
        distance: int = None,
        remove: str = None,
        filter: str = None,
        onfail: str = "cache",
        url_modifier: str = "notam/",
    ) -> Notam:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=location,
            args=args,
        )

        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Notam(**r[1])

    def parse_notam(
        self,
        notam: str,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/notam",
    ) -> Notam:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=notam,
            include_main=False,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True, data=notam, method="POST")
        return Notam(**r[1])

    def get_nbm(
        self,
        report: str,
        location: str,
        options: str = None,
        airport: bool = None,
        reporting: bool = None,
        remove: str = None,
        filter: str = None,
        onfail: str = "cache",
        url_modifier: str = "nbm/",
    ) -> Nbm:
        args = locals()
        url = url_builder(
            url_modifier=f"{url_modifier}{report}/",
            base_url=BASE_URL,
            main_payload=location,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Nbm(**r[1])

    def parse_nbm(
        self,
        nbm: str,
        report: str,
        options: str,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/nbm",
    ) -> Nbm:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=report,
            include_main=True,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True, data=nbm, method="POST")
        return Nbm(**r[1])

    def get_gfs(
            self,
            report: str,
            location: str,
            options: str = None,
            airport: bool = None,
            reporting: bool = None,
            remove: str = None,
            filter: str = None,
            onfail: str = "cache",
            url_modifier: str = "gfs/",
    ) -> Gfs:
        args = locals()
        url = url_builder(
            url_modifier=f"{url_modifier}{report}/",
            base_url=BASE_URL,
            main_payload=location,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return Gfs(**r[1])

    def parse_gfs(
            self,
            gfs: str,
            report: str,
            options: str,
            remove: str = None,
            filter: str = None,
            url_modifier: str = "parse/gfs",
    ) -> Gfs:
        args = locals()
        url = url_builder(
            url_modifier=url_modifier,
            base_url=BASE_URL,
            main_payload=report,
            include_main=True,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True, data=gfs, method="POST")
        return Gfs(**r[1])
