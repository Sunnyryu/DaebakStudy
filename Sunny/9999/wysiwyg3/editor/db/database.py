import pymysql
import os
import csv
from dotenv import load_dotenv

load_dotenv()
class Database:
    def db_connect():
        pw = os.getenv("PASSWORD")
        user = os.getenv("USER")
        db = os.getenv("DB")
        print(pw)
        print(user)
        print(db)
        conn = pymysql.connect(host='localhost',
                                 user= user,
                                 password= pw,
                                 db=db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
        cursor = conn.cursor()
        return conn, cursor
    def IndexValueread():
        try:
            if conn:
                with conn.cursor() as cursor:
                    sql = '''
                    SELECT handle, title, image_src, variant_price FROM product
                    '''
                    a = cursor.execute(sql)
                    rows = cursor.fetchall()
                conn.commit()

        except Exception as e:
            print('->', e)
            rows= None
        finally:
            if conn:
                conn.close()
        return rows
