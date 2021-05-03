import json

import config as config
from flask import Blueprint, request, jsonify
from movie.infrastructure.request import Request
from movie.infrastructure.rabbitmq import RabbitMq

from movie.infrastructure.db import MovieRegistryPostgre

movie_bp = Blueprint('movie', __name__)


@movie_bp.route('/movie', methods=['GET'])
def movie():
    rmq = RabbitMq()
    rmq.get_message()
    return {
        "response": True,
        "movies": json.loads(rmq.message)
    }


@movie_bp.route('/movie/import', methods=['GET'])
def movie_import():
    try:
        req = Request(config.OMDB_API['KEY'], config.OMDB_API['URL'], MovieRegistryPostgre())
        return jsonify(
            req.import_movie(
                {
                    's': request.args.get('s'),
                    'page': request.args.get('page'),
                    'apikey': request.args.get('apikey')
                }
            )
        )
    except KeyError:
        return jsonify({'Response': False})
