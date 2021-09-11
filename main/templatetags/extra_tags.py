from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.filter(name='range')
def get_range(start, end):
    try:
        return range(start, end)
    except TypeError:
        return []
    
@register.filter(name='time_since')
def time_since(date):
    seconds = round((datetime.now().timestamp() - date))
    interval = seconds / 31536000

    if interval > 1:
        return str(round(interval)) + " лет назад"
    
    interval = seconds / 2592000
    if interval > 1: 
        return str(round(interval)) + " месяцев назад"
    
    interval = seconds / 86400
    if interval > 1:
        return str(round(interval)) + " дней назад"
    interval = seconds / 3600
    if interval > 1:
        return str(round(interval)) + " часов назад"
    interval = seconds / 60
    if interval > 1:
        return str(round(interval)) + " минут назад"
    else:
        return str(round(seconds)) + " секунд назад"
