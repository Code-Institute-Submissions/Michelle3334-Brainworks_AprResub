"""Home app views"""
from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def braintease(request):
    """ A view to return the braintease page """
    return render(request, 'braintease/braintease.html')
