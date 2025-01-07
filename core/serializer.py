from rest_framework import serializers

from core.models import Agency, Astronaut, Planet, Mission, Spacecraft


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'

class AstronautSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astronaut
        fields = '__all__'

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class SpacecraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spacecraft
        fields = '__all__'