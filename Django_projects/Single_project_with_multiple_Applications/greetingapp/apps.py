from django.apps import AppConfig
from django.http import HttpResponse


class GreetingappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greetingapp'


# Create your views here.
def wish_view(request):
    return HttpResponse('<h1>Hello Good Morning </h1>')
