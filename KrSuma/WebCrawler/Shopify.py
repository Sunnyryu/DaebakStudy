# main program
# usage : run shopify.py, then enter the url of the vendor site.

import csv
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


def get_page_option(input_url, page, collection_handle=None):
    pass


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


def extract_products_options(input_url, path, collections=None):
    pass


def extract_products_collection(url, col):
    page = 1
    # products = get_page_option(url, page, col)
    products = get_page(url, page)
    while products:
        for product in products:
            title = product['title']
            product_type = product['product_type']
            # product_url = url + '/products/' + product['handle']
            product_handle = product['handle']
            product_vendor = product['vendor']
            # product_tags = product['tags']

            for i, variant in enumerate(product['variants']):
                variant_price = variant['price']
                option1_name = variant['option1'] or ''
                option2_name = variant['option2'] or ''
                option3_name = variant['option3'] or ''
                # option_value = ' '.join([option1_value, option2_value, option3_value]).strip()
                variant_sku = variant['sku']
                variant_compare_at_price = variant['compare_at_price']
                variant_requires_shipping = variant['requires_shipping']
                variant_grams = variant['grams']
                variant_taxable = variant['taxable']
                main_image_src = ''
                if product['images']:
                    main_image_src = product['images'][0]['src']

                image_src = get_image(variant['id'], product) or main_image_src
                stock = 'Yes'
                if not variant['available']:
                    stock = 'No'

                # row = {'variant_sku': variant_sku,
                #        'product_type': product_type,
                #        'title': title,
                #        'option1_value': option1_value,
                #        'option2_value': option2_value,
                #        'option3_value': option3_value,
                #        'price': variant_price,
                #        'stock': stock,
                #        'body': str(product['body_html']),
                #        'variant_id': product_handle + str(variant['id']),
                #        'product_handle': product_handle,
                #        'product_url': product_url,
                #        'image_src': image_src}

                row = {'Handle': product_handle,
                       'Title': title,
                       'Body (HTML)': str(product['body_html']),
                       'Vendor': product_vendor,
                       'Type': product_type,
                       'Tags': '',
                       'Published': '',
                       'Option1 Name': str(option1_name),
                       'Option1 Value': '',
                       'Option2 Name': str(option2_name),
                       'Option2 Value': '',
                       'Option3 Name': str(option3_name),
                       'Option3 Value': '',
                       'Variant SKU': variant_sku,
                       'Variant Grams': str(variant_grams),
                       'Variant Inventory Tracker': '',
                       'Variant Inventory Policy': '',
                       'Variant Fulfillment Service': '',
                       'Variant Price': variant_price,
                       'Variant Compare At Price': str(variant_compare_at_price),
                       'Variant Requires Shipping': str(variant_requires_shipping),
                       'Variant Taxable': str(variant_taxable),
                       'Variant Barcode': '',
                       'Image Src': image_src,
                       'Image Position': '',
                       'Image Alt Text': '',
                       'Gift Card': '',
                       'SEO Title': '',
                       'SEO Description': '',
                       'Google Shopping/Google Product Category': '',
                       'Google Shopping/Gender': '',
                       'Google Shopping/Age Group': '',
                       'Google Shopping/MPN': '',
                       'Google Shopping/AdWords Grouping': '',
                       'Google Shopping/AdWords Label': '',
                       'Google Shopping/Condition': '',
                       'Google Shopping/Custom Product': '',
                       'Google Shopping/Custom Label 0': '',
                       'Google Shopping/Custom Label 1': '',
                       'Google Shopping/Custom Label 2': '',
                       'Google Shopping/Custom Label 3': '',
                       'Google Shopping/Custom Label 4': '',
                       'Variant Image': '',
                       'Variant Weight Unit': '',
                       'Variant Tax Code': '',
                       'Cost per item': str(0)
                       }

                for k in row:
                    row[k] = str(row[k].strip()) if row[k] else ''
                yield row

        page += 1
        # products = get_page_option(url, page, col)
        products = get_page(url, page)


def extract_products(input_url, path):
    print("Running...")
    tic = time.perf_counter()
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(['Code',
        #                  'Collection',
        #                  'Category',
        #                  'Name',
        #                  'Variant Name',
        #                  'Price',
        #                  'In Stock',
        #                  'URL',
        #                  'Image URL',
        #                  'Body'])

        writer.writerow(['Handle',
                         'Title',
                         'Body (HTML)',
                         'Vendor',
                         'Type',
                         'Tags',
                         'Published',
                         'Option1 Name',
                         'Option1 Value',
                         'Option2 Name',
                         'Option2 Value',
                         'Option3 Name',
                         'Option3 Value',
                         'Variant SKU',
                         'Variant Grams',
                         'Variant Inventory Tracker',
                         'Variant Inventory Policy',
                         'Variant Fulfillment Service',
                         'Variant Price',
                         'Variant Compare At Price',
                         'Variant Requires Shipping',
                         'Variant Taxable',
                         'Variant Barcode',
                         'Image Src',
                         'Image Position',
                         'Image Alt Text',
                         'Gift Card',
                         'SEO Title',
                         'SEO Description',
                         'Google Shopping/Google Product Category',
                         'Google Shopping/Gender',
                         'Google Shopping/Age Group',
                         'Google Shopping/MPN',
                         'Google Shopping/AdWords Grouping',
                         'Google Shopping/AdWords Label',
                         'Google Shopping/Condition',
                         'Google Shopping/Custom Product',
                         'Google Shopping/Custom Label 0',
                         'Google Shopping/Custom Label 1',
                         'Google Shopping/Custom Label 2',
                         'Google Shopping/Custom Label 3',
                         'Google Shopping/Custom Label 4',
                         'Variant Image',
                         'Variant Weight Unit',
                         'Variant Tax Code',
                         'Cost per item'
                         ])

        seen_variants = set()
        for col in get_page_collections(input_url):
            # if collections and col['handle'] not in collections:
            #     continue
            handle = col['handle']
            title = col['title']
            for product in extract_products_collection(input_url, handle):
                # variant_id = product['variant_id']
                # if variant_id in seen_variants:
                #     continue
                #
                # seen_variants.add(variant_id)

                # writer.writerow([product['sku'],  # code
                #                  str(title),  # collection
                #                  product['product_type'],  # category
                #                  product['title'],  # name
                #                  product['option_value'],  # variant name
                #                  product['price'],  # price
                #                  product['stock'],  # in stock
                #                  product['product_url'],  # url
                #                  product['image_src'],  # image url
                #                  product['body']  # body
                #                  ])

                writer.writerow([product['Handle'],
                                 product['Title'],
                                 product['Body (HTML)'],
                                 product['Vendor'],
                                 product['Type'],
                                 product['Tags'],
                                 product['Published'],
                                 product['Option1 Name'],
                                 product['Option1 Value'],
                                 product['Option2 Name'],
                                 product['Option2 Value'],
                                 product['Option3 Name'],
                                 product['Option3 Value'],
                                 product['Variant SKU'],
                                 product['Variant Grams'],
                                 product['Variant Inventory Tracker'],
                                 product['Variant Inventory Policy'],
                                 product['Variant Fulfillment Service'],
                                 product['Variant Price'],
                                 product['Variant Compare At Price'],
                                 product['Variant Requires Shipping'],
                                 product['Variant Taxable'],
                                 product['Variant Barcode'],
                                 product['Image Src'],
                                 product['Image Position'],
                                 product['Image Alt Text'],
                                 product['Gift Card'],
                                 product['SEO Title'],
                                 product['SEO Description'],
                                 product['Google Shopping/Google Product Category'],
                                 product['Google Shopping/Gender'],
                                 product['Google Shopping/Age Group'],
                                 product['Google Shopping/AdWords Grouping'],
                                 product['Google Shopping/AdWords Label'],
                                 product['Google Shopping/Condition'],
                                 product['Google Shopping/Custom Product'],
                                 product['Google Shopping/Custom Label 0'],
                                 product['Google Shopping/Custom Label 1'],
                                 product['Google Shopping/Custom Label 2'],
                                 product['Google Shopping/Custom Label 3'],
                                 product['Google Shopping/Custom Label 4'],
                                 product['Variant Image'],
                                 product['Variant Weight Unit'],
                                 product['Variant Tax Code'],
                                 product['Cost per item']
                ])

    toc = time.perf_counter()
    print('Elapsed time: {toc-tic:0.4f} seconds')


user_input = str(input('Enter the website: '))
url = validate_url(user_input)
# collections = []
extract_products(url, 'products.csv')
print('Finished')
