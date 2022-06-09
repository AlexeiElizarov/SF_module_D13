from django.urls import path
from .views import Advertsement, index

urlpatterns = [
    path('', index, name='advertsement'),
]
