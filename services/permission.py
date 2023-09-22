from flask import Blueprint, request

from mock_engine import Engine
from model import *

permission = Blueprint('permission', __name__)

engine = Engine()


@permission.route('/api/permission/list', methods=['GET'])
def get_permission_list():
    res = engine.find(Permission)
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': [d.model_dump(by_alias=True) for d in res]}


@permission.route('/api/permission/add', methods=['POST'])
def add_permission():
    obj = Permission(**request.get_json())
    if engine.find_one(Permission, {'action': obj.action, 'type': obj.dtype}):
        return {'code': 400, 'msg': 'already exist'}
    engine.create(Permission, obj)
    return {'code': 200, 'msg': 'success'}


@permission.route('/api/permission/delete', methods=['DELETE'])
def delete_permission():
    d = request.get_json()
    for oid in d:
        engine.delete(Permission, oid)
    return {'code': 200, 'msg': 'success'}


@permission.route('/api/permission/update', methods=['PUT'])
def update_permission():
    obj = Permission(**request.get_json())
    engine.update(Permission, obj)
    return {'code': 200, 'msg': 'success'}
