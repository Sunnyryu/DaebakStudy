import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def Get_vendor(handle):
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
                SELECT DISTINCT vendor FROM product where handle = %s
                '''
                a = cursor.execute(sql, handle)
                rows = cursor.fetchall()
                vendor_get = rows[0]['vendor']
            connection.commit()

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return vendor_get