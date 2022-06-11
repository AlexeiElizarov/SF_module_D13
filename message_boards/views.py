from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from django.views import View

class Advertsement(View):
   template_name = 'message_boards/page.html'


def index(request: HttpRequest) -> HttpResponse:
    print('***************', settings.BASE_DIR)
    return render(request, 'message_boards/page.html')