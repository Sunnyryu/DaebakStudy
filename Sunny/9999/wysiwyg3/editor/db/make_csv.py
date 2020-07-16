import pymysql
import os
import csv
import pandas as pd
from dotenv import load_dotenv
import datetime
load_dotenv()

def Make_csv():
    pw = os.getenv("PASSWORD")
    user = os.getenv("USER")
    db = os.getenv("DB")
    connection = None
    rows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= user,
                                 password= pw,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                vendor = 'banharimarket'
                sql = f'''
                SELECT handle, title, body_HTML, vendor, type, tags, published, option1_name, option1_value, option2_name, option2_value, 
                                option3_name, option3_value, variant_sku, variant_grams, variant_inventory_tracker, variant_inventory_qty, variant_inventory_policy, variant_fullfillment_service, variant_price, variant_compare_at_price, varient_requires_shipping, variant_taxable, 
                                variant_barcord, image_src, image_position, image_alt_text, gift_card, seo_title, seo_description, google_shopping_google_product_category, google_shopping_gender, goggle_shopping_age_group, google_shopping_mpn, google_shopping_adwords_grouping, 
                                google_shopping_adwords_labels, google_shopping_condition, google_shopping_custom_product, google_shopping_custion_label0, google_shopping_custion_label1, google_shopping_custion_label2, google_shopping_custion_label3, google_shopping_custion_label4, variant_image, variant_weight_unit, variant_tax_code, cost_per_item 
                                FROM product where vendor = '{vendor}'
                '''													
                a = cursor.execute(sql)
                b = f'make_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
            connection.commit()
            result = pd.read_sql_query(sql,connection)
            result.rename(columns={'handle': 'Handle', 'title': 'Title', 'body_HTML':'Body (HTML)','vendor':'Vendor', 'type':'Type', 'tags':'Tags', 'published':'Published', 'option1_name':'Option1 Name', 'option1_value':'Option1 Value',
                'option2_name':'Option2 Name', 'option2_value':'Option2 Value', 'option3_name':'Option3 Name', 'option3_value':'Option3 Value', 'variant_sku':'Variant SKU', 'variant_grams':'Variant Grams', 'variant_inventory_tracker':'Variant Inventory Tracker',
                'variant_inventory_qty':'Variant Inventory Qty', 'variant_inventory_policy':'Variant Inventory Policy','variant_fullfillment_service':'Variant Fulfillment Service', 'variant_price':'Variant Price', 'variant_compare_at_price':'Variant Compare At Price',
                'varient_requires_shipping':'Variant Requires Shipping', 'variant_taxable':'Variant Taxable', 'variant_barcode':'Variant Barcode', 'image_src':'Image Src', 'image_position':'Image Position', 'image_alt_text':'Image Alt Text',
                'gift_card':'Gift Card', 'seo_title':'SEO Title', 'seo_description':'SEO Description', 'google_shopping_google_product_category':'Google Shopping / Google Product Category', 'google_shopping_gender':'Google Shopping / Gender',
                'google_shopping_age_group':'Google Shopping / Age Group', 'google_shopping_mpn':'Google Shopping / MPN', 'google_shopping_adwords_grouping':'Google Shopping / AdWords Grouping', 'google_shopping_adwords_labels':'Google Shopping / AdWords Labels',
                'google_shopping_condition':'Google Shopping / Condition', 'google_shopping_custom_product':'Google Shopping / Custom Product', 'google_shopping_custom_label_0':'Google Shopping / Custom Label 0', 'google_shopping_custion_label1':'Google Shopping / Custom Label 1',
                'google_shopping_custion_label2':'Google Shopping / Custom Label 2', 'google_shopping_custion_label3':'Google Shopping / Custom Label 3', 'google_shopping_custion_label4':'Google Shopping / Custom Label 4',
                'variant_image':'Variant Image', 'variant_weight_unit':'Variant Weight Unit', 'variant_tax_code':'Variant Tax Code', 'cost_per_item':'Cost per item'  }, inplace=True)
            result.to_csv(rf'{b}.csv',index=False)
            

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows
