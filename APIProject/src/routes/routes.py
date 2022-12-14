from flask import Blueprint, send_file, request, jsonify

from src.controllers import controllers
from src.middleware import middleware
from src.config.config import app, db, ma, basedir
from src.models.sonification import *
from src.models.user import *
from src.models import sonification
import os


def test_connection():
    with app.app_context():
        #db.drop_all()
        db.create_all()
        new_user(345345345, "Name", "Lastname")


@app.route('/', methods=['GET', 'POST'])
def index():
    #test_connection()
    return jsonify({"message": "Benvenuto nelle API per la sonificazione."})


@app.route('/audio/new', methods=['POST'])
def generate_audio():
    request_data = request.get_json()
    headers = request.headers
    response = middleware.middleware(request_data, headers)
    if response:
        return app.response_class(
            response="Parametri mancanti. Controllare la richiesta",
            status=400,
            mimetype='application/json'
        )
    audio = controllers.generate_audio()

    new_file(audio, request_data["type"], request_data["order"], request_data["instrument"], request_data["length"], headers["access-token"])
    return send_file(
        os.path.join(basedir, '..', '..', audio),
        mimetype='audio/wav'
    )


@app.route("/", methods=["GET"])
def new():
    return new_file()


@app.route("/audio/all", methods=["GET"])
def get_all():
    if(request.headers["access-token"] == ""):
        return app.response_class(
            response="Parametri mancanti. Controllare la richiesta",
            status=400,
            mimetype='application/json'
        )
    return list_all(request.headers["access-token"])


@app.route("/all/info/<id>", methods=["GET"])
def get_info_file(id):
    return get_by_id(id)


@app.route("/audio/<id>", methods=["GET"])
def get_file(id):
    file = get_file_by_id(id)
    if file:
        return send_file(
            os.path.join(basedir, '..', '..', file),
            mimetype='audio/wav'
        )
    else:
        return app.response_class(
            response="File non trovato",
            status=400,
            mimetype='application/json'
        )


@app.route("/audio/<id>", methods=["DELETE"])
def remove_file(id):
    if(request.headers["access-token"] == ""):
        return app.response_class(
            response="Parametri mancanti. Controllare la richiesta",
            status=400,
            mimetype='application/json'
        )
    return sonification.remove_file_by_id(id)
