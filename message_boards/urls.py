from django.urls import path
from .views import AdvertsementListView, AdvertsementCreateView

urlpatterns = [
    # path('', index, name='advertsement'),
    path('advertsement/', AdvertsementListView.as_view(), name='advertsement_list'),
    path('advertsement/create/', AdvertsementCreateView.as_view(), name='advertsement_create'),
]
