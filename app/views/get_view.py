from flask import Flask


def init_app(app: Flask):

    @app.get("/posts")
    def get_all_posts():
        ...
    # get all published posts

    @app.get("/posts/<int:id>")
    def get_post_by_id(post_id):
        ...
    # get posts by specific id
