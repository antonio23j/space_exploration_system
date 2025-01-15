from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Agency, Astronaut, Planet, Mission, Spacecraft
from core.serializer import AgencySerializer, AstronautSerializer, PlanetSerializer, MissionSerializer, \
    SpacecraftSerializer


# Create your views here.
class AgencyViewSet(ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer

    @action(detail=True, methods=['get'])
    def missions(self, request):
        """
        Get all missions for an agency.
        """
        try:
            agency = self.get_object()
            missions = agency.missions.all()
            return Response({"missions": [mission.name for mission in missions]}, status=status.HTTP_200_OK)
        except Agency.DoesNotExist:
            return Response({"error": "Agency not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def astronauts(self, request):
        """
        Get all astronauts associated with an agency.
        """
        try:
            agency = self.get_object()
            astronauts = agency.astronauts.all()
            return Response({"astronauts": [astronaut.name for astronaut in astronauts]}, status=status.HTTP_200_OK)
        except Agency.DoesNotExist:
            return Response({"error": "Agency not found."}, status=status.HTTP_404_NOT_FOUND)


class AstronautViewSet(ModelViewSet):
    queryset = Astronaut.objects.all()
    serializer_class = AstronautSerializer


class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    @action(detail=True, methods=['get'])
    def missions(self, request, pk=None):
        """
        Get all missions visiting this planet.
        """
        try:
            planet = self.get_object()
            missions = planet.missions.all()
            return Response({"missions": [mission.name for mission in missions]}, status=status.HTTP_200_OK)
        except Planet.DoesNotExist:
            return Response({"error": "Planet not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def spacecrafts(self, request, pk=None):
        """
        Get all spacecrafts that visited this planet.
        """
        try:
            planet = self.get_object()
            spacecrafts = planet.spacecrafts.all()
            return Response({"spacecrafts": [spacecraft.name for spacecraft in spacecrafts]}, status=status.HTTP_200_OK)
        except Planet.DoesNotExist:
            return Response({"error": "Planet not found."}, status=status.HTTP_404_NOT_FOUND)


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @action(detail=True, methods=['get'])
    def missions(self, request, pk=None):
        """
        Get all missions visiting this planet.
        """
        try:
            planet = self.get_object()
            missions = planet.missions.all()
            return Response({"missions": [mission.name for mission in missions]}, status=status.HTTP_200_OK)
        except Planet.DoesNotExist:
            return Response({"error": "Planet not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def add_spacecraft(self, request, pk=None):
        """
        Add a spacecraft to a mission.
        """
        spacecraft_id = request.data.get("spacecraft_id")
        try:
            mission = self.get_object()
            spacecraft = Spacecraft.objects.get(id=spacecraft_id)
            mission.spacecraft.add(spacecraft)
            return Response({"message": f"Spacecraft {spacecraft.name} added to Mission {mission.name}."},
                            status=status.HTTP_200_OK)
        except Spacecraft.DoesNotExist:
            return Response({"error": "Spacecraft not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def spacecrafts(self, request):
        """
        List all spacecrafts in a mission.
        """
        try:
            mission = self.get_object()
            spacecrafts = mission.spacecraft.all()
            return Response({"spacecrafts": [spacecraft.name for spacecraft in spacecrafts]}, status=status.HTTP_200_OK)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'])
    def astronauts(self, request, pk=None):
        """
        Get all astronauts involved in a mission.
        """
        try:
            mission = self.get_object()
            astronauts = mission.astronauts.all()
            return Response({"astronauts": [astronaut.name for astronaut in astronauts]}, status=status.HTTP_200_OK)
        except Mission.DoesNotExist:
            return Response({"error": "Mission not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['delete'])
    def remove_spacecraft(self, request):
        """
        Remove a spacecraft from a mission.
        """
        spacecraft_id = request.data.get("spacecraft_id")
        try:
            mission = self.get_object()
            spacecraft = Spacecraft.objects.get(id=spacecraft_id)
            mission.spacecraft.remove(spacecraft)
            return Response({"message": f"Spacecraft {spacecraft.name} removed from Mission {mission.name}."},
                            status=status.HTTP_200_OK)
        except Spacecraft.DoesNotExist:
            return Response({"error": "Spacecraft not found."}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['post'])
    def add_astronaut(self, request, pk=None):
        """
        Add an astronaut to a mission.
        """
        astronaut_id = request.data.get("astronaut_id")
        try:
            mission = self.get_object()
            astronaut = Astronaut.objects.get(id=astronaut_id)
            mission.astronauts.add(astronaut)
            return Response({"message": f"Astronaut {astronaut.name} added to Mission {mission.name}."},
                            status=status.HTTP_200_OK)
        except Astronaut.DoesNotExist:
            return Response({"error": "Astronaut not found."}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['delete'])
    def remove_astronaut(self, request, pk=None):
        """
        Remove an astronaut from a mission.
        """
        astronaut_id = request.data.get("astronaut_id")
        try:
            mission = self.get_object()
            astronaut = Astronaut.objects.get(id=astronaut_id)
            mission.astronauts.remove(astronaut)
            return Response({"message": f"Astronaut {astronaut.name} removed from Mission {mission.name}."},
                            status=status.HTTP_200_OK)
        except Astronaut.DoesNotExist:
            return Response({"error": "Astronaut not found."}, status=status.HTTP_404_NOT_FOUND)

class SpacecraftViewSet(ModelViewSet):
    queryset = Spacecraft.objects.all()
    serializer_class = SpacecraftSerializer