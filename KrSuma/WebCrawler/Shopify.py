import csv
import json
import time
import urllib.request
from urllib.error import HTTPError


def retry():
    print('Blocked! Sleeping...')
    time.sleep(180)
    print('Retrying')


def validate_url(input_url):
    fixed_url = input_url.strip()
    if not fixed_url.startswith('http://') and not fixed_url.startswith('https://'):
        fixed_url = 'https://' + fixed_url
    return fixed_url.rstrip('/')


def get_page(input_url, page, collection_handle=None):
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


def get_image(variant_id, product):
    images = product['images']
    for i in images:
        k = [str(v) for v in i['variant_ids']]
        if str(variant_id) in k:
            return i['src']
    return ''


def get_page_collections(url):
    full_url = url + '/collections.json'
    page = 1
    while True:
        req = urllib.request.Request(full_url + '?page={}'.format(page))
        while True:
            try:
                data = urllib.request.urlopen(req).read()
                break
            except HTTPError:
                retry()

        cols = json.loads(data.decode())['collections']
        if not cols:
            break
        for col in cols:
            yield col
        page += 1


def check_shopify(input_url):
    try:
        get_page(input_url, 1)
        return True
    except Exception:
        return False


def extract_products_collection(url, col):
    page = 1
    products = get_page(url, page, col)
    while products:
        for product in products:
            title = product['title']
            product_type = product['product_type']
            product_url = url + '/products/' + product['handle']
            product_handle = product['handle']

            for i, variant in enumerate(product['variants']):
                price = variant['price']
                option1_value = variant['option1'] or ''
                option2_value = variant['option2'] or ''
                option3_value = variant['option3'] or ''
                option_value = ' '.join([option1_value, option2_value, option3_value]).strip()
                sku = variant['sku']
                main_image_src = ''
                if product['images']:
                    main_image_src = product['images'][0]['src']

                image_src = get_image(variant['id'], product) or main_image_src
                stock = 'Yes'
                if not variant['available']:
                    stock = 'No'

                row = {'sku': sku, 'product_type': product_type,
                       'title': title, 'option_value': option_value,
                       'price': price, 'stock': stock, 'body': str(product['body_html']),
                       'variant_id': product_handle + str(variant['id']),
                       'product_url': product_url, 'image_src': image_src}
                for k in row:
                    row[k] = str(row[k].strip()) if row[k] else ''
                yield row

        page += 1
        products = get_page(url, page, col)


def extract_products(input_url, path, collections=None):
    with open(path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Code', 'Collection', 'Category',
                         'Name', 'Variant Name',
                         'Price', 'In Stock', 'URL', 'Image URL', 'Body'])
        seen_variants = set()
        for col in get_page_collections(input_url):
            # if collections and col['handle'] not in collections:
            #     continue
            handle = col['handle']
            title = col['title']
            for product in extract_products_collection(input_url, handle):
                variant_id = product['variant_id']
                if variant_id in seen_variants:
                    continue

                seen_variants.add(variant_id)
                writer.writerow([product['sku'], str(title),
                                 product['product_type'],
                                 product['title'], product['option_value'],
                                 product['price'],
                                 product['stock'], product['product_url'],
                                 product['image_src'], product['body']])


user_input = input("Enter the website: ")
args = str(user_input)
url = validate_url(args)
collections = []
print("Running...")
extract_products(url, 'products.csv', collections)

