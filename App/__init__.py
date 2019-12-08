from flask import Flask
from App.view import init_view
from App.ext import init_ext
from App.config import envs


def create_app(env):
    app = Flask(__name__, static_folder='../static', template_folder='../templates')

    app.config.from_object(envs.get(env))
    init_view(app)
    init_ext(app)

    return app