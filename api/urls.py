from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('relays/', views.relays, name='relays'),
]
