import requests


def get_content_type(url):
    r = requests.get('{}'.format(url))
    return r.headers['content-type']