from flask import Flask
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["kenzie"]

db.posts.insert_one({"test": "hi"})


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return "<h1>Hello flask</h1>"

    return app
