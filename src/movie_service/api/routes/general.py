from flask import Blueprint, jsonify

general = Blueprint('general', __name__)


@general.route('/', methods=['GET'])
def index():
    return jsonify(
        {
            'status': True,
            'message': 'It works!',
        }
    )


@general.route('/health', methods=['GET'])
def health_check():
    return jsonify(
        {
            'status': True
        }
    )
