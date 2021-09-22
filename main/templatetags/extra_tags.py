from django import template
from datetime import datetime
from allauth.socialaccount.models import SocialAccount

register = template.Library()


@register.filter(name='get_profile_pic_src')
def get_profile_pic_src(message_user):
    if not message_user:
        return '/static/oauth/anonymous.png'
    elif message_user.is_staff:
        return '/static/oauth/admin_avatar.jpg'
    else:
        social_account = SocialAccount.objects.get(user_id=message_user.id)
        provider = social_account.provider
        if provider == 'vk':
            return social_account.extra_data['photo_medium']
        elif provider == 'google':
            return social_account.extra_data['picture']
        elif provider == 'facebook':
            return f'https://graph.facebook.com/{social_account.uid}/picture?type=large'


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
