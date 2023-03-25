from django.http import HttpResponse


def home(request):
    return HttpResponse('<center><h1>Home</h1></center>')
