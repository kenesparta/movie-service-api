from waitress import serve

import config
from app import app, register_routes

if __name__ == "__main__":
    register_routes()
    serve(app, listen=config.APP['LISTEN'])
