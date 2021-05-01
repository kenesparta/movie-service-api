from flask import Flask

import config

app = Flask(__name__)

app.config.update(
    TESTING=config.APP['TESTING'],
    SECRET_KEY=config.APP['SECRET_KEY']
)
