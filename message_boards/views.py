import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.views import View
from django.views.generic import ListView, CreateView
from .models import Advertsement
from .forms import AdvertsementForm


# class AdvertsementView(View):
#    template_name = 'message_boards/page.html'


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'message_boards/page.html', context={'var': os.environ})


class AdvertsementListView(ListView):
    model = Advertsement
    template_name = 'message_boards/advertsements_list_all.html'
    context_object_name = 'advertsements'
    paginate_by = 10
    # добавляем форм класс, чтобы получать доступ к форме через метод POST


class AdvertsementCreateView(LoginRequiredMixin, CreateView):
    model = Advertsement
    form_class = AdvertsementForm
    template_name = 'message_boards/advertsement_create.html'
    success_url = '/news/'
