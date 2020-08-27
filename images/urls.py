from django.urls import path, include
from .views import *

app_name = 'images'

urlpatterns = [
    path('create/', image_create, name='create'),
]
