import re
import os
from django.conf import settings
from django.utils.html import escape


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


def strip_tags(html):
    # Strip HTML tags from any string and transfrom special entities.
    text = html
    print(text)

    # Apply rules in given order.
    rules = [
        {r'>\s+': u'>'},  # Remove spaces after a tag opens or closes.
        {r'\s+': u' '},  # Replace consecutive spaces.
        {r'\s*<br\s*/?>\s*': u'\n'},  # Newline after a <br>.
        {r'</(div)\s*>\s*': u'\n'},  # Newline after </p> and </div> and <h1/>.
        {r'</(p|h\d)\s*>\s*': u'\n\n'},  # Newline after </p> and </div> and <h1/>.
        {r'<head>.*<\s*(/head|body)[^>]*>': u''},  # Remove <head> to </head>.
        {r'<a\s+href="([^"]+)"[^>]*>.*</a>': r'\1'},  # Show links instead of texts.
        {r'[ \t]*<[^<]*?/?>': u''},  # Remove remaining tags.
        {r'^\s+': u''}  # Remove spaces at the beginning.
    ]

    # Replace special strings.
    special = {
        '&nbsp;': ' ', '&amp;': '&', '&quot;': '"',
        '&lt;': '<', '&gt;': '>', '</div><div>': '::br::',
        '<div>': '::br::',
    }

    for (k, v) in special.items():
        text = text.replace(k, v)

    print(text)

    for rule in rules:
        for (k, v) in rule.items():
            try:
                regex = re.compile(k)
                text = regex.sub(v, text)
            except:
                pass  # Pass up whatever we don't find.

    text = text.replace('::br::', '<br>')

    return text


def sanitize(text):
    text = strip_tags(text)
    return text
