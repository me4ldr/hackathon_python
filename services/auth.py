import datetime

from flask import Blueprint, request, make_response, session

import config
from mock_engine import Engine, get_user_model
from model import *
import jwt

auth = Blueprint('auth', __name__)

engine = Engine()


# @auth.route('/')
# def index():
#     return 'welcome'


@auth.route('/api/auth/login', methods=['POST'])
def login():
    d = request.get_json()
    model = get_user_model(d['identity'])
    user = engine.find_one(model, {engine.pk_map.get(model): d['account']})
    if not user:
        return {'code': 1, 'msg': 'user not found'}
    if d['password'] != user.password:
        return {'code': 2, 'msg': 'incorrect password'}

    res = make_response({'code': 200, 'msg': 'login success'})
    exp = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    token_data = {
        'account': d['account'],
        'identity': d['identity'],
        'exp': exp.timestamp(),
    }
    token = jwt.encode({'data': token_data, 'exp': exp}, config.SECRET_KEY, algorithm='HS256')
    res.set_cookie('uid', token, expires=exp)
    return res


@auth.route('/api/auth/code', methods=['GET'])
def code():
    return {'code': 200, 'msg': 'success', 'data': None}
