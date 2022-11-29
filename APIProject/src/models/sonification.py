from flask import jsonify
from sqlalchemy.sql import func
from src.util.const import *
from src.routes.routes import db, ma
import os


class Sonification(db.Model):
    __tablename__ = "sonification"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    file_type = db.Column(db.String(100), nullable=False)
    order = db.Column(db.String(100), nullable=False)
    instrument = db.Column(db.String(100), nullable=False)
    length = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, name, file_type, order, instrument, length, user_id):
        self.name = name
        self.file_type = file_type
        self.order = order
        self.instrument = instrument
        self.length = length
        self.user_id = user_id


def new_file(name, file_type, order, instrument, length, user_id):
    new_sonification = Sonification(name, file_type, order, instrument, length, user_id)
    db.session.add(new_sonification)
    db.session.commit()
    return sonification_schema.jsonify(new_sonification)


def remove_file_by_id(id):
    info_file = get_by_id(id)
    db.session.delete(info_file)
    db.session.commit()
    basedir = os.path.abspath(os.path.dirname(__file__))
    os.remove(os.path.join(info_file.name))
    return jsonify({"message": "File eliminato."})

def get_file_by_id(id):
    sonification = Sonification.query.get(id)
    if(sonification):
        return directory_wav + sonification.name + '.flac'
    else:
        return None


def get_by_id(id):
    return Sonification.query.get(id)


def list_all(user_id):
    all_files = Sonification.query.filter_by(user_id=user_id).all()
    results = sonifications_schema.dump(all_files)
    print(all_files)
    return jsonify(results)


class SonificationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'file_type', 'order', 'instrument', 'length', 'created_at')


# Initialize Schema
sonification_schema = SonificationSchema()
sonifications_schema = SonificationSchema(many=True)
