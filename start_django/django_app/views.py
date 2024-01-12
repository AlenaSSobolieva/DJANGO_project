# django_app/views.py

# from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

    # return HttpResponse('Hello! You are at django_app page')


