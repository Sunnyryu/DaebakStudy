import pandas as pd
from sqlalchemy import create_engine
import os
import pymysql
import MySQLdb
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("PASSWORD")
db = os.getenv("DB")
db_id = os.getenv("ID")

engine = create_engine(f'mysql+mysqldb://{db_id}:'+password+f'@localhost/{db}', encoding='utf-8')
conn =engine.connect()

csv_test = pd.read_csv('C:/Users/tusik/Desktop/123/DaebakStudy/Sunny/Python/prep/db_prep/BRND-hyunavely-Top-233items.csv', encoding='1250')
csv_test.to_sql(name="tusi_table", con=engine, if_exists='append')
