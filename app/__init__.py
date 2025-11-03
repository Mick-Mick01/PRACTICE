from flask import Flask

app = Flask(__name__)

from .dashboard import dash_bp

def app1():
    app.register_blueprint(dash_bp, url_prefix="/")
    return app