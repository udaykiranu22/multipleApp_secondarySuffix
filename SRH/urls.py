from django.urls import path
from SRH.views import *


urlpatterns = [
    path('captain/', captain, name='captain'),
    path('wicketkeeper/', wicketkeeper, name='wicketkeeper'),
    path('vicecaptain/', vicecaptain, name='vicecaptain'),
]