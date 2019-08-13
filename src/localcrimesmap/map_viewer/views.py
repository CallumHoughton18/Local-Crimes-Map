from django.shortcuts import render
from common.utils import get_month_intervals

def RenderMap(request):
    months = get_month_intervals()
    return render(request, "map_viewer/map.html", {'monthIntervals':months})
