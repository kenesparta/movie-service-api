from waitress import serve

import config
from api.routes.general import general
from app import app


def __register_routes():
    app.register_blueprint(general)


if __name__ == "__main__":
    __register_routes()
    serve(app, listen=config.APP['LISTEN'])
