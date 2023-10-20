import pyavwx
import time


api = pyavwx.AvwxApiClient("")
api = api.get_metar(location="LFPX", options="info")

print(api.info)


