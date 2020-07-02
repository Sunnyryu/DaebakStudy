import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def VendorSearch(vendor_get):
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
                SELECT DISTINCT handle, title FROM product where vendor = %s
                '''
                a = cursor.execute(sql, vendor_get)
                rows = cursor.fetchall()
                print(rows)
                #handlelist = []
                #for row in rows:
                #    handlelist.append(row['handle'])
                #    handlelist.sort()
            connection.commit()

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows