import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def HandleSearch(handle):
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
                SELECT * FROM product where handle = %s
                '''
                a = cursor.execute(sql, handle)
                rows = cursor.fetchall()
                #idlist = []
                #titlelist = []
                #body_HTMLlist = []
                #vendorlist = []
                #taglist = []
                #publishedlist = []
                #option1_namelist = []
                #option2_namelist = []
                #option3_namelist = []
                #option1_valuelist = []
                #option2_valuelist = []
                #option3_valuelist = []
                #variant_skulist = []
                #variant_pricelist = []
                #variant_compare_at_pricelist = []
                #image_srclist = []
                #cost_per_itemlist = []

                #for row in rows:
                #    idlist.append(row['id'])
                #    titlelist.append(row['title'])
                #    body_HTMLlist.append(row['body_HTML'])
                #    vendorlist.append(row['vendor'])
                #    taglist.append(row['tags'])
                #    publishedlist.append(row['published'])
                #    option1_namelist.append(row['option1_name'])
                #    option2_namelist.append(row['option2_name'])
                #    option3_namelist.append(row['option3_name'])
                #    option1_valuelist.append(row['option1_value'])
                #    option2_valuelist.append(row['option2_value'])
                #    option3_valuelist.append(row['option3_value'])
                #    variant_skulist.append(row['variant_sku'])
                #    variant_pricelist.append(row['variant_price'])
                #    variant_compare_at_pricelist.append(row['variant_compare_at_price'])
                #    image_srclist.append(row['image_src'])
                #    cost_per_itemlist.append(row['cost_per_item']) 
            connection.commit()

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    #return idlist, titlelist, body_HTMLlist, vendorlist, taglist, publishedlist, option1_namelist, option2_namelist, option3_namelist,
    #option1_valuelist, option2_valuelist, option3_valuelist, variant_skulist, variant_pricelist, variant_compare_at_pricelist,
    #image_srclist, cost_per_itemlist,
    return rows