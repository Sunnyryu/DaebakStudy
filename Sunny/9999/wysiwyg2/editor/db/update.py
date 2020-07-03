
import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def Update_table_main(value_new_id, value_new_title, value_new_body_HTML, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time):
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

                sql = "UPDATE product Set title=%s, body_HTML=%s, option1_value =%s, variant_price=%s, revise=%s, revise_last_time=%s where id = %s"

                a = cursor.execute(sql,(value_new_title, value_new_body_HTML, value_new_option1_value, value_new_price, value_new_revise_times, value_new_revise_last_time, value_new_id))

                rows = cursor.fetchall()
                connection.commit()
                    
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows



def Update_table_etc(value_new_id, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time):
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
                sql = "UPDATE product Set option1_value =%s, variant_price=%s, revise=%s, revise_last_time=%s  where id = %s"
                a = cursor.execute(sql,(value_new_option1_value, value_new_price, value_new_revise_times, value_new_revise_last_time, value_new_id))
                rows = cursor.fetchall()
                connection.commit()
                    
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()

    return rows