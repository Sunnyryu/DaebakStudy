from flask import Flask
from dotenv import load_dotenv
import os 

load_dotenv(verbose=True)
secret_key = os.getenv("SECRET_KEY")
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

from lotto import routes