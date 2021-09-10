import re
import os
from django.conf import settings


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
            text = text.replace(f'<img src="/static/images/{match}.png" width="28" height="28">', f':{match}:">')
    return text


def sanitize(text):
    return re.sub(r'[^\w ,.():-]*', '', text)
