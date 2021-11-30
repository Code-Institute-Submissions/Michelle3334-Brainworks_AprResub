"""Cart app views"""
from django.shortcuts import render


def view_cart(request):
    """ Cart contents page view"""

    return render(request, 'cart/cart.html')
