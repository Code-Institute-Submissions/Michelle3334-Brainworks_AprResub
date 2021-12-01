"""Tool to calculate subtotal for shopping cart"""
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """Calculation for subtotal"""
    return price * quantity
