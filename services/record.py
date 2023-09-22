from flask import Blueprint, request

from mock_engine import Engine
from model import *

record = Blueprint('record', __name__)

engine = Engine()


@record.route('/api/record/list', methods=['GET'])
def get_record_list():
    res = engine.find(Record)
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': [d.model_dump() for d in res]}


@record.route('/api/record/add', methods=['POST'])
def add_record():
    obj = Record(**request.get_json())
    engine.create(Record, obj)
    return {'code': 200, 'msg': 'success'}


@record.route('/api/record/delete', methods=['DELETE'])
def delete_record():
    d = request.get_json()
    for oid in d:
        engine.delete(Record, oid)
    return {'code': 200, 'msg': 'success'}


@record.route('/api/record/update', methods=['PUT'])
def update_record():
    obj = Record(**request.get_json())
    engine.update(Record, obj)
    return {'code': 200, 'msg': 'success'}
