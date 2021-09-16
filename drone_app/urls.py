from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("drone/category", views.DronesCategoriesView)
router.register("drone", views.DronesView)
router.register("pilot", views.PilotsView)
router.register("competitions", views.CompetitionsView)

urlpatterns = [
    path("", include(router.urls))
]
