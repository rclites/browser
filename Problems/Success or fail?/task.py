import requests


def check_success(url):
    r = requests.get('{}'.format(url))
    if 199 < r.status_code < 400:
        return 'Success'
    return 'Fail'
