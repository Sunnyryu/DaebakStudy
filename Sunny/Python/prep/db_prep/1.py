import pymysql
from datetime import datetime

print('START TIME : ',str(datetime.now())[10:19] )

def fwrite():
    with open('a.csv','a') as f:
        f.writelines(text[:-1]+'\n')   ## 각 row 맨 마지막 , 제거용

conn=pymysql.connect(host='localhost',port=3306,user='root',password='12345678',db='tusi')
c=conn.cursor()

sql="select * from tusi_table"
c.execute(sql)
rows=c.fetchall()

for i in rows:    
    text=''
    for j in i:
        j=str(j)
        text=text+j+','
    fwrite()

print('END TIME : ',str(datetime.now())[10:19] )

c.close()
conn.close()