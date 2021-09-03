from flask import Flask
from app.models.Post import db


def init_app(app: Flask):

    @app.get("/posts")
    def get_all_posts():
        data = list(db.posts.find())
        for object in data:
            del object["_id"]
        print(data)
        return data, 200
    # get all published posts

    @app.get("/posts/<int:id>")
    def get_post_by_id(post_id):
        ...
    # get posts by specific id
