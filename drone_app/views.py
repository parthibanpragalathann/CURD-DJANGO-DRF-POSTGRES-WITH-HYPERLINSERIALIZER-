from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import update_last_login
from .pagination import CustomPageNumberPageination, CursorPaginationWithOrdering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.contrib.auth.models import User
from .serializer import RegisterSerializer, LoginSerializer, PasswordSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

class PasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

#DRONE Source
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
    #permission_classes = [IsAuthenticated]
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name',)
    search_fields = ('name',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

class DronesView(viewsets.ModelViewSet):
    queryset = Drones.objects.order_by("name")
    serializer_class = DronesSerializer
    #permission_classes = [AllowAny]
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('created_at',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

class PilotsView(viewsets.ModelViewSet):
    queryset = Pilots.objects.order_by("name")
    serializer_class = PilotsSerializer
    #permission_classes = [AllowAny]
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name', 'gender')
    search_fields = ('name', 'gender')
    ordering_fields = ('number_race',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

class CompetitionsView(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer
    #permission_classes = [AllowAny]
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('drone', 'pilot')
    search_fields = ('drone', 'pilot', 'date')
    ordering_fields = ('distance',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering
