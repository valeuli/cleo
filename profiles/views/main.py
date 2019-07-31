from django.shortcuts import render

"""
    a ver si funcion
"""


def index(request):
    return render(request, 'profiles/index.html')
