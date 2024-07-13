from flask import Flask
from .extensions import *

def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    from .resource_api import SatuResource
    api.add_resource(SatuResource, "/satu")

    # inisialisasi extension
    api.init_app(app)
    # db.init_app(app)
    # api.init_app(app)

    # registrasi blueprint
    from .rute import my_bp
    
    # app.register_blueprint(my_bp, url_prefix="/contoh")
    app.register_blueprint(my_bp, url_prefix="/")


    # @app.route("")
    # def index():
    #     return "ini adalah index"

    # print(app.url_map)

    return app