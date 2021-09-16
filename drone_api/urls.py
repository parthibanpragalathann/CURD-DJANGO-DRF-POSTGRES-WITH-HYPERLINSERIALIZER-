from django.urls import path, include

urlpatterns = [
    path('api/', include('drone_app.urls'))  #Following the path of drone app site URLs
]