from flask import Flask, request
from app.models.Post import Post


def init_app(app: Flask):
    @app.post("/posts")
    def publish_new_post():
        data = request.json
        try:
            post = Post(**data)
            post.save()
            return post.serialized(), 201
        except:
            return {"msg": "Post inválido"}, 406
        # 406 - not acceptable?

    @app.patch("/posts/<int:id>")
    def update_post(id: int):
        Post.update_post_by_id(id, request.json)
        return request.json, 200

    @app.delete("/posts/<int:id>")
    def delete_post(id: int):
        post = Post.delete_post_by_id(id)
        if post:
            return {"msg": ""}, 204
        return {"msg": "Post not found"}, 404
