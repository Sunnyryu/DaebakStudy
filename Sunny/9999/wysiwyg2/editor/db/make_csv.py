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
                sql = '''
                SELECT handle, title, body_HTML, vendor, type, tags, published, option1_name, option1_value, option2_name, option2_value, 
                              option3_name, option3_value, variant_sku, variant_grams, variant_inventory_tracker, variant_inventory_qty, variant_inventory_policy, variant_fullfillment_service, variant_price, variant_compare_at_price, varient_requires_shipping, variant_taxable, 
                              variant_barcord, image_src, image_position, image_alt_text, gift_card, seo_title, seo_description, google_shopping_google_product_category, google_shopping_gender, goggle_shopping_age_group, google_shopping_mpn, google_shopping_adwords_grouping, 
                              google_shopping_adwords_labels, google_shopping_condition, google_shopping_custom_product, google_shopping_custion_label0, google_shopping_custion_label1, google_shopping_custion_label2, google_shopping_custion_label3, google_shopping_custion_label4, variant_image, variant_weight_unit, variant_tax_code, cost_per_item 
                              FROM product
                '''
                a = cursor.execute(sql)
                b = f'make_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
            connection.commit()
            result = pd.read_sql_query(sql,connection)
            result.to_csv(rf'{b}.csv',index=False)
            

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows
