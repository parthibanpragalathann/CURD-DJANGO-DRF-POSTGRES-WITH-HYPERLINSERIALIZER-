
from rest_framework import serializers
from .models import *

class DronesCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DronesCategory
        fields = ("id", "url", "name")

class DronesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drones
        fields = ("id", "url", "name", "drone_category", "manufacture_date", "is_participated", "created_at")

class PilotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pilots
        fields = ("id", "url", "name", "gender", "number_race", "created_at")

class CompetitionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competitions
        fields = ("id", "url", "drone", "pilot", "distance", "date")
