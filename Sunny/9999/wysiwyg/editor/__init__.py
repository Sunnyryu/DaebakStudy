from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os 

load_dotenv(verbose=True)
secret_key = os.getenv("SECRET_KEY")
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@localhost:3306/{db_name}'
db_url = f'mysql://{username}:{password}@localhost:3306/{db_name}'
db = SQLAlchemy(app)
print(app.config['SQLALCHEMY_DATABASE_URI'])

from editor import routes
