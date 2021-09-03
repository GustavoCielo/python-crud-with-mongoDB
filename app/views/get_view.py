from flask import Flask, jsonify
from app.models.Post import Post


def init_app(app: Flask):

    @app.get("/posts")
    def get_all_posts():
        """route to get all published posts"""
        posts = Post.get_all()
        return jsonify(posts), 200

    @app.get("/posts/<int:id>")
    def get_post_by_id(id: int):
        """route to get posts specified by id through url params"""
        post = Post.get_post_by_id(id)
        return jsonify(post), 200
