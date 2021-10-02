import re
import os
from django.conf import settings
from django.utils.html import escape
from io import StringIO
from html.parser import HTMLParser


def replace(text):
    q = re.findall(r'(?<=:)\w+', text)
    for match in q:
        if os.path.exists(settings.STATICFILES_DIRS[0] + '/images/' + match + '.png'):
            text = text.replace(f":{match}:", '<img class="emoji" src="/static/images/' + match + '.png">')
    return text


def replace_image_with_smiles(text):
    q = re.findall(r'(?<=<img src="/static/images/)\w+', text)
    for match in q:
        if os.path.exists(settings.STATICFILES_DIRS[0] + '/images/' + match + '.png'):
            text = text.replace(f'<img src="/static/images/{match}.png" width="28" height="28">', f':{match}:')
    return text
    
    
def sanitize(text):
    text = escape(text).replace('&lt;/div&gt;&lt;div&gt;','<br>')
    text = text.replace('&lt;div&gt;','<br>')
    text = text.replace('&lt;/div&gt;', '')
    text = text.replace('&lt;br&gt;', '')
    text = text.replace('&lt;', '').replace('&gt;', '').replace('script', '').replace("&nbsp;", "")
    return text
    