from django import template

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
