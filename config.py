# config.py
import os


class Config:
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "6f4151593c59448cdb325593557e0d3b823970e03f2698747be65d0df6036bee"
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
