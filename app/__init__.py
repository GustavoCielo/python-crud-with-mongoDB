from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.views import get_view, post_view

    get_view.init_app(app)

    post_view.init_app(app)

    return app
