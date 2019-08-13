from datetime import datetime,date, timedelta
from .constants import EARTH_RADIUS_MILES
from math import atan2, acos, cos, sin, asin, radians, degrees

def get_month_intervals():
    startdate = date(2005,1,1)
    enddate =  date.today() - timedelta(30)
    monthsList = []

    total_months = lambda dt: dt.month + 12 * dt.year

    for tot_m in range(total_months(startdate)-1, total_months(enddate)):
        year, month = divmod(tot_m, 12)
        monthsList.append(datetime(year, month+1, 1).strftime('%Y-%m'))

    monthsList.reverse()
    return monthsList

def get_month_intervals_as_tuple():
    return tuple((item, item) for item in get_month_intervals())

def add_miles_to_lat_lng(lat, lng, bearing, miles):
    latRadian = radians(lat)
    lngRadian = radians(lng)
    bearingRadian = radians(bearing)

    lat2Radians = asin(sin(latRadian) * cos(miles/EARTH_RADIUS_MILES) + cos(latRadian) * sin(miles/EARTH_RADIUS_MILES) * cos(bearingRadian))
    lng2Radians = lngRadian + atan2(sin(bearingRadian) * sin(miles/EARTH_RADIUS_MILES) * cos(latRadian), cos(miles/EARTH_RADIUS_MILES) - sin(latRadian) * sin(lat2Radians))

    lat2Degrees = degrees(lat2Radians)
    lng2Degrees = degrees(lng2Radians)

    return (lat2Degrees, lng2Degrees)
