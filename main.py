# THIS API RETURNS COUNTRY'S ECONOMIC, SOCIAL CONDITION DATA

from flask import Flask
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello Worlds'


if __name__ == "__main__":
    app.run(debug=True)