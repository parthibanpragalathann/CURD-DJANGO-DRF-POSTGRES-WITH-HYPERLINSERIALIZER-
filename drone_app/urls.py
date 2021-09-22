from django.urls import path, include
from rest_framework import routers
from . import views
from knox import views as knox_views
from .views import *

router = routers.DefaultRouter()
router.register("drone/category", views.DronesCategoriesView) #drone category urls
router.register("drone", views.DronesView)  #drone urls
router.register("pilot", views.PilotsView)  #pilot urls
router.register("competitions", views.CompetitionsView) #competitions

#api application urls ...
urlpatterns = [
    path("", include(router.urls)),
    path('register/', CustomUserRegister.as_view(), name="customuser_register"),
    # Authentication CustomUser Register urls.
    path('login/', CustomUserLogin.as_view(), name="CustomUser_Login"),  # Authentication CustomUser Login urls.
    path('users/', CustomUserView.as_view(), name="CustomUserview"),  # Authentication CustomUser details urls.
    path('user/<int:pk>', CustomUserModify.as_view(), name='CustomUserupdate'),
    # Authentication CustomUser update&delete urls.
    path('changepwd/', CustomUserChangePassword.as_view(), name='changepwd'),
    # Authentication CustomUser changing password urls.
    # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    # #Authentication CustomUser Knox Logout urls.
    path('option/logout/', CustomUserLogout.as_view(), name="optional_logout"),
    # Authentication CustomUser optional Logout urls.
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    # Authentication CustomUser Knox Logout AllSite urls.

]
