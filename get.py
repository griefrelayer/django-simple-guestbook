import requests
import re
import os
from django.conf import settings

site = 'https://www.wysiwygwebbuilder.com/support/bootstrapguestbook/'

fp = open('templates/index.html')
lines = fp.readlines()
fp.close()


def search(arr):
    out = []
    for x in arr:
        q = re.search(r'(?<=/assets/emoji/)[\w/\-.]+', x)
        if q:
            out.append(q.group(0))
    return out


def replace(arr):
    out = []
    for line in arr:
        q = re.search(r'(?<=src=")[\w/\-.]+', line)
        if q:
            line = line.replace(q.group(0), '{% static "' + q.group(0) + '" %}')
        out.append(line)
    return out


'''urls = search(lines)

for src_url in urls:

    with open('static/'+src_url, 'wb') as handle:
        response = requests.get(site+src_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
    print('got ' + src_url)'''

fp = open('templates/smiles.html', 'w')
fp.writelines(replace(lines))
fp.close()
