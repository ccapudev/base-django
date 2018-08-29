from django.urls import path
from apps.usuarios import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('jwt/', obtain_jwt_token, name='token')
]