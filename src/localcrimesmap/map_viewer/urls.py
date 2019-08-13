from django.urls import path, include
from .views import RenderMap

urlpatterns = [
    path('', RenderMap, name='map'),
]