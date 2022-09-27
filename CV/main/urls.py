from django.urls import path
from .views import *
urlpatterns = [
    path('', index), #main page with snake
    path('about', about), #page for me
]
