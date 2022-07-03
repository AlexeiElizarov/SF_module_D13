import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Advertsement
from .forms import AdvertsementForm

from typing import Any, Dict
from sign.models import MyUser

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'message_boards/page.html', context={'var': os.environ})


class AdvertsementListView(ListView):
    '''Вьюха отображает все объявления'''
    model = Advertsement
    template_name = 'message_boards/advertsements_list_all.html'
    context_object_name = 'advertsements'
    paginate_by = 10
    # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            'adversements': Advertsement.objects.all(),

        }


class AdvertsementsUser(ListView):
    '''Вьюха отображает все объявления текущего юзера'''
    model = Advertsement
    template_name = 'message_boards/advertsements_list_user.html'
    context_object_name = 'advertsements'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        user_id = MyUser.objects.get(username=self.request.user).id
        return {
            **super().get_context_data(*args, **kwargs),
            'advertsements': Advertsement.objects.filter(user_id=user_id)
        }


class AdvertsementCreateView(LoginRequiredMixin, CreateView):
    '''Вьюха создания нового объявления'''
    model = Advertsement
    form_class = AdvertsementForm
    template_name = 'message_boards/advertsement_create.html'
    # success_url = '/news/'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> "HttpResponse":
        form = self.form_class(request.POST)
        if form.is_valid():
            advertsement = Advertsement(
                title=request.POST['title'],
                body=request.POST['body'],
                category=request.POST['category'],
                user_id=MyUser.objects.get(username=request.user.username).id
            )
            advertsement.save()
        return redirect('advertsement_list')


class AdvertsementUpdateView(LoginRequiredMixin, UpdateView):
    '''Вьюха редактировантя объявления'''
    template_name = 'message_boards/advertsement_create.html'
    form_class = AdvertsementForm

    # метод get_object мы используем вместо queryset,
    # чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertsement.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['is_authors'] = self.request.user.groups.filter(name='authors').exists()
        return context


class AdvertsementDetailView(DetailView):
    '''Вьюха детелизации объявления'''
    model = Advertsement
    template_name = 'message_boards/advertsement_detail.html'
    context_object_name = 'advertsement'
    success_url = 'adversement/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertsement.objects.get(pk=id)



