import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch7 import Elasticsearch, exceptions


es = Elasticsearch(hosts=['elasticsearch'])
while True:
    try:
        es.search(index="posts")
        break
    except (
        exceptions.ConnectionError,
        exceptions.TransportError
    ):
        time.sleep(1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pg:pass@database:5432/post_search"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

from search import models
from search import routes
