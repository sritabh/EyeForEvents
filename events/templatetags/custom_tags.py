from django import template

register = template.Library()

#Custom tag to subtract two numbers
@register.filter
def subtract(value, arg):
    return int(value) - len(arg)