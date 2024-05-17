# Creating views using function
from django.http import HttpRequest, HttpResponse


def greet(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, have a good day and better tomorrow!')


def greet_name(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse('Hello, ' + name + '! Welcome to my blog.')
