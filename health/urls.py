from django.urls import path
from . import views

urlpatterns = [
    path('', views.uptime_info, name='datetimeView'),
]
