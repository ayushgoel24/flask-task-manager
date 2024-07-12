# app/main/__init__.py
from flask import Blueprint

bp = Blueprint("main", __name__, template_folder="templates", static_folder="static")

from app.main import routes
