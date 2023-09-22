from flask import Blueprint, request

from mock_engine import Engine, get_user_model
from model import *
from utils.jwt_util import get_identity

user = Blueprint('user', __name__)

engine = Engine()


@user.route('/api/get_user', methods=['GET'])
def get_user():
    identity, account, role, _ = get_identity(request.cookies)

    model = get_user_model(identity)
    obj = engine.find_one(model, {engine.pk_map.get(model): account})
    permissions = [engine.find_by_id(Permission, i) for i in role.permissions]

    res = obj.model_dump()
    res['role'] = role.model_dump()
    res['permissions'] = [f'{p.dtype}:{p.action}' for p in permissions]
    return {'code': 200, 'msg': 'success', 'data': res}


@user.route('/api/user/list', methods=['GET'])
def get_permission_list():
    identity = request.args.get('type')
    model = get_user_model(identity)
    res = engine.find(model)
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': [d.model_dump(by_alias=True) for d in res]}


@user.route('/api/user/add', methods=['POST'])
def add_user():
    d = request.get_json()
    model = get_user_model(d['type'])
    obj = model(**d['data'])
    pk = engine.pk_map.get(model)
    engine.create(model, obj, getattr(obj, pk))
    return {'code': 200, 'msg': 'success'}


@user.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    d = request.get_json()
    model = get_user_model(d['type'])
    for oid in d['data']['ids']:
        engine.delete(model, oid)
    return {'code': 200, 'msg': 'success'}


@user.route('/api/user/update', methods=['PUT'])
def update_user():
    d = request.get_json()
    model = get_user_model(d['type'])
    obj = model(**d['data'])
    engine.update(model, obj)
    return {'code': 200, 'msg': 'success'}
