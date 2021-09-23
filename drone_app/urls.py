from django.urls import path, include
from rest_framework import routers
from . import views
from knox import views as knox_views
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
router = routers.DefaultRouter()
router.register("drone/category", views.DronesCategoriesView) #drone category urls
router.register("drone", views.DronesView)  #drone urls
router.register("pilot", views.PilotsView)  #pilot urls
router.register("competitions", views.CompetitionsView) #competitions

#api application urls ...
urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('refresh/', TokenRefreshView.as_view(), name='auth_refresh'),
    path('password/<int:pk>/', PasswordView.as_view(), name='auth_change_password'),
    path('profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]
