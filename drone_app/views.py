from rest_framework import viewsets
from .models import *
from .serializer import *
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import update_last_login
from .pagination import CustomPageNumberPageination, CursorPaginationWithOrdering
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
class CustomUserRegister(generics.GenericAPIView):  # Authentication CustomUser Register View.
    permission_classes = [AllowAny]
    serializer_class = CustomUserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class CustomUserView(APIView):  # class member details view here(Read Only.)
    serializer_class = CustomUserupdelSerializer
    permission_classes = [AllowAny]
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

    def get(self, request, *args, **kwargs):
        info = CustomUser.objects.order_by("username")
        serializer = CustomUserupdelSerializer(info, many=True)
        return Response(serializer.data)


class CustomUserModify(APIView):  # class of CustomUser details update && delete view here
    permission_classes = [AllowAny]
    serializer_class = CustomUserupdelSerializer
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, pk, format=None):
        detail = self.get_object(pk)
        serializer = CustomUserupdelSerializer(detail)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = CustomUserupdelSerializer(info, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        info_delete = self.get_object(pk)
        info_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Authentication CustomUser Login View.
class CustomUserLogin(generics.GenericAPIView):
    serializer_class = CustomUserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        update_last_login(None, user)
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class CustomUserChangePassword(generics.UpdateAPIView):  # Authentication CustomUser changing password View.
    serializer_class = CustomUserChangePasswordSerializer
    model = CustomUser
    permission_classes = [AllowAny]
    #permission_classes = (permissions.IsAuthenticated,)
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            confirm_password = serializer.data.get('confirm_password')
            new_password = serializer.data.get('new_password')
            if new_password == confirm_password:
                self.object.set_password(new_password)
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }
                return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLogout(APIView):  # Authentication CustomUser optional Logout View.
    def get(self, request, format=None):
        # using Django logout
        logout(request)
        return Response(status=status.HTTP_200_OK)

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
    permission_classes = [AllowAny]
    #permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name',)
    search_fields = ('name',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

class DronesView(viewsets.ModelViewSet):
    queryset = Drones.objects.order_by("name")
    serializer_class = DronesSerializer
    permission_classes = [AllowAny]
    #permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name',)
    search_fields = ('name',)
    ordering_fields = ('created_at',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

class PilotsView(viewsets.ModelViewSet):
    queryset = Pilots.objects.order_by("name")
    serializer_class = PilotsSerializer
    permission_classes = [AllowAny]
    #permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('name', 'gender')
    search_fields = ('name', 'gender')
    ordering_fields = ('number_race',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering

class CompetitionsView(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer
    permission_classes = [AllowAny]
    #permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ('drone', 'pilot')
    search_fields = ('drone', 'pilot', 'date')
    ordering_fields = ('distance',)
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering
