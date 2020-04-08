# test for extracting the json from shopify api

import json
import time
import urllib.request
from urllib.error import HTTPError

set_sleep = 60


def retry():
    print('Blocked! Retrying in ' + str(set_sleep) + ' seconds.')
    time.sleep(set_sleep)
    print('Retrying...')


def validate_url(input_url):
    fixed_url = input_url.strip()
    if not fixed_url.startswith('http://'):
        fixed_url = 'https://' + fixed_url
        print("URL set to " + fixed_url)
    return fixed_url.rstrip('/')


def get_page(input_url, page):
    full_url = input_url
    # if collection_handle:
    #     full_url += '/collections/{}'.format(collection_handle)
    full_url += '/products.json'
    req = urllib.request.Request(full_url + '?page={}'.format(page))
    while True:
        try:
            data = urllib.request.urlopen(req).read()
            break
        except HTTPError:
            retry()

    products = json.loads(data.decode())['products']
    return products

user_input = str(input('Enter the website: '))
url = validate_url(user_input)
print(get_page(url, 1))
