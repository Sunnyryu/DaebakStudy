from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os 

load_dotenv(verbose=True)
secret_key = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = #'mysql://사용자:비밀번호@도메인:3306/서비스이름'
db = SQLAlchemy(app)
from editor import routes
