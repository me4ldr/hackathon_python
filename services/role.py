from flask import Blueprint, request

from mock_engine import Engine
from model import *

role = Blueprint('role', __name__)

engine = Engine()


@role.route('/api/role/list', methods=['GET'])
def get_role_list():
    res = engine.find(Role)
    res = [Role(**r.model_dump()) for r in res]
    for r in res:
        permissions = [engine.find_by_id(Permission, i) for i in r.permissions]
        r.permissions = permissions
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': [d.model_dump(by_alias=True) for d in res]}


@role.route('/api/role/add', methods=['POST'])
def add_role():
    obj = Role(**request.get_json())
    engine.create(Role, obj)
    return {'code': 200, 'msg': 'success'}


@role.route('/api/role/delete', methods=['DELETE'])
def delete_role():
    d = request.get_json()
    for oid in d:
        engine.delete(Role, oid)
    return {'code': 200, 'msg': 'success'}


@role.route('/api/role/update', methods=['PUT'])
def update_role():
    obj = Role(**request.get_json())
    engine.update(Role, obj)
    return {'code': 200, 'msg': 'success'}
