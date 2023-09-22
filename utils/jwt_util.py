import jwt

import config
from mock_engine import Engine, get_user_model
from model import Role

engine = Engine()


def get_identity(cookie):
    decoded = jwt.decode(cookie.get("uid"), config.SECRET_KEY, algorithms=['HS256'])
    identity = decoded['data']['identity']
    account = decoded['data']['account']
    model = get_user_model(identity)
    obj = engine.find_one(model, {engine.pk_map.get(model): account})
    role = engine.find_by_id(Role, obj.role_id)
    return identity, account, role, obj.name
