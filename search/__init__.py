from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from elasticsearch7 import Elasticsearch


es = Elasticsearch(['localhost'])
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pg:pass@localhost:5432/post_search"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

from search import models
from search import routes
