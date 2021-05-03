from flask import Flask

import config
from api.routes import general, movie

app = Flask(__name__)

app.config.update()


def register_routes():
    app.register_blueprint(general.general)
    app.register_blueprint(movie.movie_bp)
