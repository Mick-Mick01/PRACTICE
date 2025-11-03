from flask import Blueprint

dash_bp = Blueprint("dashboard", __name__)

from . import routes