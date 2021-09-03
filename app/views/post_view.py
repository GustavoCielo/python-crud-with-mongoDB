from flask import Flask, request
from app.models.Post import Post


def init_app(app: Flask):
    @app.post("/posts")
    def publish_new_post():
        data = request.json
        # try:
        post = Post(**data)
        post.save()
        return post.serialized(), 200
        # except:
        #     return {"msg": "Post inválido"}, 400

    @app.patch("/posts/<int:id>")
    def update_post():
        ...
        # update an existing post

    @app.delete("/posts/<int:id>")
    def delete_post(id: int):
        post = Post.delete_post_by_id(id)
        if post:
            return {"msg": ""}, 204
        return {"msg": "Post not found"}, 404
