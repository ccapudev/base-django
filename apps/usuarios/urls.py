from django.urls import path
from apps.usuarios import views


urlpatterns = [
    path('', views.home, name='home')
]