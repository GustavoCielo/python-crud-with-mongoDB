from flask import Flask


def init_app(app: Flask):
    @app.post("/posts")
    def publish_new_post():
        ...
        # publish a new post containing all informations

    @app.patch("/posts/<int:id>")
    def update_post():
        ...
        # update an existing post

    @app.delete("/posts/<int:id>")
    def delete_post():
        ...
        # delete an existing post
