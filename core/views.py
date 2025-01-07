from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from core.models import Agency, Astronaut, Planet, Mission, Spacecraft
from core.serializer import AgencySerializer, AstronautSerializer, PlanetSerializer, MissionSerializer, \
    SpacecraftSerializer


# Create your views here.
class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

class AstronautViewSet(ModelViewSet):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer


class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class SpacecraftViewSet(ModelViewSet):
    queryset = Spacecraft.objects.all()
    serializer_class = SpacecraftSerializer