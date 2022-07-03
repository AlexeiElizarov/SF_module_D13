from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='advertsement'),
    path('', AdvertsementListView.as_view(), name='advertsement_list'),
    path('create/', AdvertsementCreateView.as_view(), name='advertsement_create'),
    path('<int:pk>/', AdvertsementDetailView.as_view(), name='advertsement_detail'),
    path('<int:pk>/edit/', AdvertsementUpdateView.as_view(), name='advertsement_edit'),
    path('user/', AdvertsementsUser.as_view(), name='advertsement_user'),
]

