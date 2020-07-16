import pymysql
import os
import csv
from dotenv import load_dotenv
load_dotenv()

def ValueSearch(vendor):
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
                SELECT DISTINCT * FROM product where vendor = %s
                '''
                a = cursor.execute(sql, vendor)
                rows = cursor.fetchall()
            connection.commit()

    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows
