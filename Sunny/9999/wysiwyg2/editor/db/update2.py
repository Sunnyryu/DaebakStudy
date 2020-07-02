
import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def Update_table_main(value_new_id, value_new_price, value_new_option1_value, value_new_title, value_new_body_HTML):
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
                print(1)
                sql = "UPDATE product Set title=%s body_HTML=%s option1_value =%s variant_price=%s  where id = %s"
                #sql = '''
                #UPDATE product Set title = %s, body_HTML =%s, option1_value=%s, option2_value=%s, variant_price=%s
                #where id = %s
                #'''
                #print(value2['id'][i])
                #print(value2['variant_price'][i])
                a = cursor.execute(sql,(value_new_title, value_new_body_HTML, value_new_option1_value, value_new_price, value_new_id))
                print(a)
                #a = cursor.execute(sql, value2['title'][i], value2['body_HTML'][i], value2['option1_value'][i], value2['option2_value'][i], value2['price'][i], value2['id'][i])
                rows = cursor.fetchall()
                connection.commit()
                print(2)
                    
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
def Update_table_etc(value_new_id, value_new_price, value_new_option1_value):
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
                print(1)
                sql = "UPDATE product Set option1_value =%s variant_price=%s  where id = %s"
                #sql = '''
                #UPDATE product Set title = %s, body_HTML =%s, option1_value=%s, option2_value=%s, variant_price=%s
                #where id = %s
                #'''
                #print(value2['id'][i])
                #print(value2['variant_price'][i])
                a = cursor.execute(sql,(value_new_option1_value, value_new_price, value_new_id))
                print(a)
                #a = cursor.execute(sql, value2['title'][i], value2['body_HTML'][i], value2['option1_value'][i], value2['option2_value'][i], value2['price'][i], value2['id'][i])
                rows = cursor.fetchall()
                connection.commit()
                print(2)
                    
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