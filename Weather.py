#Fetch weather data from NOAA
# setup the connection
from pydap.client import open_url


url = 'http://nomads.ncdc.noaa.gov/dods/NCEP_NARR_DAILY/197901/197901/narr-a_221_197901dd_hh00_000'
modelconn = open_url(url)
tmp2m = modelconn['tmp2m']

# grab the data
lat_index = 200    # you could tie this to tmp2m.lat[:]
lon_index = 200    # you could tie this to tmp2m.lon[:]
print tmp2m.array[:,lat_index,lon_index]