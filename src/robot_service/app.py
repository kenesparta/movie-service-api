import json

from flask import Flask, jsonify
from db import MovieRegistryPostgre
from rabbitmq import RabbitMq

app = Flask(__name__)

app.config.update()


@app.route('/rate', methods=['GET'])
def rate():
    mrp_update_rating = MovieRegistryPostgre()
    return jsonify(
        {
            "response": True,
            "rows_updated": mrp_update_rating.update(MovieRegistryPostgre().fetch())
        }
    )


@app.route('/best', methods=['GET'])
def best():
    """
    Queues the 5 best movies from the list of movies
    :return:
    """
    mrp_update_rating = MovieRegistryPostgre()
    rmq = RabbitMq()
    best_movies = mrp_update_rating.best()
    if len(best_movies):
        rmq.send_message(json.dumps(best_movies))
    return jsonify(
        {
            "response": True,
            "message": 'queued'
        }
    )
