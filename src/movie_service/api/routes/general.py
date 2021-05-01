from flask import Blueprint, jsonify

general = Blueprint('general', __name__)


@general.route('/', methods=['GET'])
def index():
    return '<h1>It works!</h1>'


@general.route('/health', methods=['GET'])
def health_check():
    return jsonify(
        {
            'status': True
        }
    )
