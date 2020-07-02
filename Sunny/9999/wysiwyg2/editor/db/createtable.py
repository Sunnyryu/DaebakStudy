import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

def Createtable():
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
                            CREATE TABLE product2 (
                                id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                                handle VARCHAR(100) NOT NULL,
                                title VARCHAR(255) NOT NULL,
                                body_HTML TEXT NOT NULL,
                                vendor VARCHAR(100) NOT NULL,
                                type VARCHAR(100) NOT NULL,
                                tags TEXT NOT NULL,
                                published VARCHAR(100) NOT NULL,
                                option1_name VARCHAR(100) NOT NULL,
                                option1_value VARCHAR(100) NOT NULL,
                                option2_name VARCHAR(100) NOT NULL,
                                option2_value VARCHAR(100) NOT NULL,
                                option3_name VARCHAR(100) NOT NULL,
                                option3_value VARCHAR(100) NOT NULL,
                                variant_sku VARCHAR(255) NOT NULL,
                                variant_grams VARCHAR(100) NOT NULL,
                                variant_inventory_tracker VARCHAR(100) NOT NULL,
                                variant_inventory_qty VARCHAR(100) NOT NULL,
                                variant_inventory_policy VARCHAR(100) NOT NULL,
                                variant_fullfillment_service VARCHAR(100) NOT NULL,
                                variant_price VARCHAR(100) NOT NULL,
                                variant_compare_at_price VARCHAR(100) NOT NULL,
                                varient_requires_shipping VARCHAR(100) NOT NULL,
                                variant_taxable VARCHAR(100) NOT NULL,
                                variant_barcord VARCHAR(100) NOT NULL,
                                image_src VARCHAR(255) NOT NULL,
                                image_position VARCHAR(100) NOT NULL,
                                image_alt_text VARCHAR(100) NOT NULL,
                                gift_card VARCHAR(100) NOT NULL,
                                seo_title VARCHAR(100) NOT NULL,
                                seo_description VARCHAR(100) NOT NULL,
                                google_shopping_google_product_category VARCHAR(100) NOT NULL,
                                google_shopping_gender VARCHAR(100) NOT NULL,
                                goggle_shopping_age_group VARCHAR(100) NOT NULL,
                                google_shopping_mpn VARCHAR(100) NOT NULL,
                                google_shopping_adwords_grouping VARCHAR(100) NOT NULL,
                                google_shopping_adwords_labels VARCHAR(100) NOT NULL,
                                google_shopping_condition VARCHAR(100) NOT NULL,
                                google_shopping_custom_product VARCHAR(100) NOT NULL,
                                google_shopping_custion_label0 VARCHAR(100) NOT NULL,
                                google_shopping_custion_label1 VARCHAR(100) NOT NULL,
                                google_shopping_custion_label2 VARCHAR(100) NOT NULL,
                                google_shopping_custion_label3 VARCHAR(100) NOT NULL,
                                google_shopping_custion_label4 VARCHAR(100) NOT NULL,
                                variant_image VARCHAR(100) NOT NULL,
                                variant_weight_unit VARCHAR(100) NOT NULL,
                                variant_tax_code VARCHAR(100) NOT NULL,
                                cost_per_item VARCHAR(100) NOT NULL,
                                revise int NOT NULL,
                                revise_last_time VARCHAR(100) NOT NULL
                            )ENGINE=InnoDB DEFAULT CHARSET=utf8
                '''
                cursor.execute(sql)
            rows = cursor.fetchall()
                #print(rows)
            connection.commit()
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows