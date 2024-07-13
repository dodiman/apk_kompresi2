import os

class Config:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class Development_config(Config):
    SECRET_KEY = "inicontohsekretkey"
    DEBUG = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "aplikasi3"
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"

    UPLOAD_FOLDER = 'temps/'
    ALLOW_EXTENSIONS = {"png", "jpg", "pdf", "txt"}

class Testing_config(Config):
    DEBUG = True
    TESTING = True

class Production_config(Config):
    DEBUG = False