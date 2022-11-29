from flask import Flask
from src.util.const import *

app = Flask(__name__)


def middleware(request_data, headers):
    if request_data:
        return check_data('instrument', request_data, instrument_poss) or check_data('length', request_data, length_poss) \
               or 'data' not in request_data or 'order' not in request_data or 'type' not in request_data or 'access-token' not in headers


def check_data(name, request_data, where_check):
    return name not in request_data or request_data[name] not in where_check
