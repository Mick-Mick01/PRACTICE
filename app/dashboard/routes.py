from flask import *
from . import dash_bp

@dash_bp.route('/')
def Index():
    return "Hello World!"