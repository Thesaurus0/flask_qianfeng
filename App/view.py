from flask import Blueprint, render_template

blue = Blueprint('blue01', __name__)

def init_view(app):
    app.register_blueprint(blue)


@blue.route('/hello/')
def hello_world():
    return render_template('index.html')
