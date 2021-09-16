from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class DronesCategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = DronesCategory.objects.all()
        serializer = DronesCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = DronesCategory.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DronesCategorySerializer(user)
        return Response(serializer.data)

# Create Drone projects views here.
class DronesCategoriesView(viewsets.ModelViewSet):
    queryset = DronesCategory.objects.order_by("name")
    serializer_class = DronesCategorySerializer

class DronesView(viewsets.ModelViewSet):
    queryset = Drones.objects.order_by("name")
    serializer_class = DronesSerializer

class PilotsView(viewsets.ModelViewSet):
    queryset = Pilots.objects.order_by("name")
    serializer_class = PilotsSerializer

class CompetitionsView(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer
