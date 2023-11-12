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
    Gfs,
    ReportsRoute,
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
        """Get station information for an airfield or other location by ICAO ident.

        :param ident: ICAO & IATA station code
        :type ident: str
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include these keys in the response, defaults to None
        :type filter: str, optional
        :return: Info for requested ``ident``
        :rtype: Station
        """
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
        n: int = None,
        airport: bool = True,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "station/near/",
    ) -> list[NearStation]:
        """Get the nearest stations to a coordinate pair.

        :param coords: Coordinate pair Example: 28.1,-81.
        :type coords: str
        :param n: Number of stations to return, defaults to 10
        :type n: int, optional
        :param airport: Only include airports, defaults to True
        :type airport: bool, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include these keys in the response, defaults to None
        :type filter: str, optional
        :return: Nearest Stations
        :rtype: list[NearStation]
        """
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
        n: int = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "search/station",
    ) -> list[Station]:
        """Text search for stations by ICAO, IATA, name, city, and state

        :param text: Search text
        :type text: str
        :param n: Max results to return, defaults to ``10``
        :type n: int, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Stations that match the requested ``text``
        :rtype: list[Station]
        """
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
        """Get reporting stations along a flight path.

        :param route: Flight route with ICAO, navaid, and coordinate, separated by a ``;``
        :type route: str
        :param distance: Distance in nautical miles from ``route` centerline
        :type distance: int
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Stations around the given ``route``
        :rtype: StationRoute
        """
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
        """Get the current and forecasted flight conditions for a specific station by ICAO & IATA station code or a coordinate pair.

        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Summary for the requested ``ident``
        :rtype: Summary
        """
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
        return Summary(**r[1])

    def get_metar(
        self,
        location: str,
        options: str = None,
        airport: bool = True,
        reporting: bool = True,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "metar/",
    ) -> Metar:
        """Get a METAR report for an airfield or other location by ICAO, IATA ident or coordinates.

        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param airport: Only include airports, defaults to True
        :type airport: bool, optional
        :param reporting: Only include reporting stations when performing a coordinate search, defaults to True
        :type reporting: bool, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Metar for the requested ``ident``
        :rtype: Metar
        """
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
        return Metar(**r[1])

    def parse_metar(
        self,
        metar: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/metar",
    ) -> Metar:
        """Parse a METAR report

        :param metar: METAR report to parse
        :type metar: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Parsed Metar for the given ``metar``
        :rtype: Metar
        """
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

    def get_multiple_reports(
        self,
        report_type: str,
        locations: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "multi/",
    ) -> Metar | Taf | Summary:
        """Get for multiple stations a given report type

        :param report_type: Weather report type (``summary``,``metar``,``taf``)
        :type report_type: str
        :param locations: Comma-separated string of up to 10 ICAO & IATA station codes
        :type locations: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Summary for the requested ``ident``
        :rtype: Metar | Taf | Summary
        """
        args = locals()
        url = url_builder(
            url_modifier=f"{url_modifier}{report_type}/",
            base_url=BASE_URL,
            main_payload=locations,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        match report_type:
            case "metar":
                return Metar(**r[1])
            case "taf":
                return Taf(**r[1])
            case "summary":
                return Summary(**r[1])

    def get_nearest_reports(
        self,
        report_type: str,
        coords: str,
        n: int = None,
        options: str = None,
        airport: bool = True,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "near/",
    ) -> Metar | Taf:
        """Get the nearest weather reports to a coordinate pair

        :param report_type: Weather report type (``metar``,``taf``)
        :type report_type: str
        :param coords: Coordinate pair Example: 28.1,-81.
        :type coords: str
        :param n: Max results to return, defaults to ``10``
        :type n: int, optional
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param airport: Only include airports, defaults to True
        :type airport: bool, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Returns ``Metar`` or ``Taf`` depending on the chosen report type
        :rtype: Metar | Taf
        """
        args = locals()
        url = url_builder(
            url_modifier=f"{report_type}/{url_modifier}",
            base_url=BASE_URL,
            main_payload=coords,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        match report_type:
            case "metar":
                return Metar(**r[1])
            case "taf":
                return Taf(**r[1])

    def get_reports_text(
        self,
        report_type: str,
        text: str,
        n: int = None,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "search/",
    ) -> list[Metar] | list[Taf]:
        """Get weather reports by searching for stations by ICAO, IATA, name, city, and state.

        :param report_type: Weather report type (``metar``,``taf``)
        :type report_type: str
        :param text: Search text
        :type text: str
        :param n: Max results to return, defaults to ``10``
        :type n: int, optional
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a list of ``Metar`` or ``Taf`` depending on the chosen report type
        :rtype: list[Metar] | list[Taf]
        """
        args = locals()
        url = url_builder(
            url_modifier=f"{url_modifier}",
            base_url=BASE_URL,
            main_payload=report_type,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)

        report_list = []
        match report_type:
            case "metar":
                for metar in r[1]:
                    report_list.append(Metar(**metar))
            case "taf":
                for taf in r[1]:
                    report_list.append(Taf(**taf))
        return report_list

    def get_reports_route(
        self,
        report_type: str,
        route: str,
        distance: int,
        options: str = None,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "path/",
    ) -> ReportsRoute:
        """Get weather reports along a flight path.

        :param report_type: Weather report type (``metar``,``taf``,``airsigmet``,``notam``)
        :type report_type: str
        :param route: Flight route with ICAO, navaid, and coordinate, separated by a ``;``
        :type route: str
        :param distance: Distance in nautical miles from ``route`` centerline
        :type distance: int
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Returns a ReportsRoute containing route info and list of report in the chosen type.
        :rtype: ReportsRoute
        """
        args = locals()
        url = url_builder(
            url_modifier=f"{url_modifier}",
            base_url=BASE_URL,
            main_payload=report_type,
            args=args,
        )
        # We Make the request, evaluate the status code
        # And then cast the json response to the Metar Object.
        r = makeRequest(url=url, auth=self.auth, rjson=True)
        return ReportsRoute(**r[1])

    def get_taf(
        self,
        location: str,
        options: str = None,
        airport: bool = True,
        reporting: bool = True,
        remove: str = None,
        filter: str = None,
        onfail: str = None,
        url_modifier: str = "taf/",
    ) -> Taf:
        """Get the TAF for a specific station by ICAO & IATA station code or a coordinate pair.

        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param airport: Only include airports, defaults to True
        :type airport: bool, optional
        :param reporting: Only include reporting stations when performing a coordinate search, defaults to True
        :type reporting: bool, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Returns a ``Taf`` object containing the requested TAF report.
        :rtype: Taf
        """
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
        return Taf(**r[1])

    def parse_taf(
        self,
        taf: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/taf",
    ) -> Taf:
        """Parse a TAF report

        :param taf: TAF report to parse
        :type taf: str, optional
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a ``Taf`` object containing the parsed report
        :rtype: Taf
        """
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
        """Get PIREPs within 200 miles of a specific station by ICAO & IATA station code or coordinate pair.

        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Returns a ``Pirep`` object containing the requested Pirep
        :rtype: Pirep
        """
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
        return Pirep(**r[1])

    def parse_pirep(
        self,
        pirep: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/pirep",
    ) -> Pirep:
        """Parse a Pirep

        :param pirep: Pirep to parse
        :type pirep: str, optional
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a ``Pirep`` object containing the parsed Pirep.
        :rtype: Pirep
        """
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
        """Get all global AIRMET and SIGMET advisories.

        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to None
        :type onfail: str, optional
        :return: Returns a ``AirSigmet`` object containing the requested Air Sigmet.
        :rtype: AirSigmet
        """
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
        airsigmet: str,
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/airsigmet",
    ) -> AirSigmet:
        """Parse an Air Sigmet

        :param airsigmet: Air Sigmet to parse.
        :type airsigmet: str, optional
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a ``AirSigmet`` object containing the parsed Air Sigmet
        :rtype: AirSigmet
        """
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
        """Get NOTAMs that apply to a specific airport or within a specified distance of a coordinate.

        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param distance: Distance in nautical miles from ``route`` centerline, defaults to None
        :type distance: int, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to "cache"
        :type onfail: str, optional
        :return: Returns a ``Notam`` object containing the requested Notam.
        :rtype: Notam
        """
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
        """Parse a Notice to Airmen (NOTAM)

        :param notam: Notam to parse.
        :type notam: str
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a ``Notam`` object containing the parsed Notam.
        :rtype: Notam
        """
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
        airport: bool = True,
        reporting: bool = True,
        remove: str = None,
        filter: str = None,
        onfail: str = "cache",
        url_modifier: str = "nbm/",
    ) -> Nbm:
        """Get the NBM NBS report for a specific station by ICAO & IATA station code or a lat,lon coordinate pair

        :param report: NBM report type. Supported: (``nbh``, ``nbs``, ``nbe``)
        :type report: str
        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param airport: Only include airports, defaults to True
        :type airport: bool, optional
        :param reporting: Only include reporting stations when performing a coordinate search, defaults to True
        :type reporting: bool, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to "cache"
        :type onfail: str, optional
        :return: Returns a ``Nbm`` object containing the requested NBM report.
        :rtype: Nbm
        """
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
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/nbm",
    ) -> Nbm:
        """Parse an NBM/NBS report

        :param nbm: NBM report to parse.
        :type nbm: str
        :param report: NBM report type. Supported: (``nbh``, ``nbs``, ``nbe``)
        :type report: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a ``Nbm`` object containing the parsed Nbm report.
        :rtype: Nbm
        """
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
        airport: bool = True,
        reporting: bool = True,
        remove: str = None,
        filter: str = None,
        onfail: str = "cache",
        url_modifier: str = "gfs/",
    ) -> Gfs:
        """Get the GFS MAV report for a specific station by ICAO & IATA station code or a coordinate pair.

        :param report: GFS report type. Supported: (``mav``, ``mex``)
        :type report: str
        :param location: ICAO & IATA station code or coordinate pair.
        :type location: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param airport: Only include airports, defaults to True
        :type airport: bool, optional
        :param reporting: Only include reporting stations when performing a coordinate search, defaults to True
        :type reporting: bool, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :param onfail: use out-of-date cache, or check nearest station when unable to fetch report, defaults to "cache"
        :type onfail: str, optional
        :return: Returns a ``Gfs`` object containing the requested GFS report.
        :rtype: Gfs
        """
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
        options: str = None,
        remove: str = None,
        filter: str = None,
        url_modifier: str = "parse/gfs",
    ) -> Gfs:
        """Parse a GFS MAV Report

        :param gfs: GFS report to parse.
        :type gfs: str
        :param report: GFS report type. Supported: (``mav``, ``mex``)
        :type report: str
        :param options: Additional options to include, defaults to None
        :type options: str, optional
        :param remove: Remove unused keys from the response, defaults to None
        :type remove: str, optional
        :param filter: Only include the selected keys in the response, defaults to None
        :type filter: str, optional
        :return: Returns a ``Gfs`` object containing the parsed GFS report.
        :rtype: Gfs
        """
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
