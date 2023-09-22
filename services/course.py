from flask import Blueprint, request

from mock_engine import Engine
from model import *
from utils.jwt_util import get_identity

course = Blueprint('course', __name__)

engine = Engine()


@course.route('/api/race/list', methods=['GET'])
def get_race_list():
    res = engine.find(Race)
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': [d.model_dump() for d in res]}


@course.route('/api/race/add', methods=['POST'])
def add_race():
    obj = Race(**request.get_json())
    engine.create(Race, obj)
    return {'code': 200, 'msg': 'success'}


@course.route('/api/race/delete', methods=['DELETE'])
def delete_race():
    d = request.get_json()
    for oid in d:
        engine.delete(Race, oid)
    return {'code': 200, 'msg': 'success'}


@course.route('/api/race/update', methods=['PUT'])
def update_race():
    obj = Race(**request.get_json())
    engine.update(Race, obj)
    return {'code': 200, 'msg': 'success'}


@course.route('/api/course/list', methods=['GET'])
def get_course_list():
    identity, account, role, _ = get_identity(request.cookies)
    race_id = request.args.get('race_id')  # ?race_id=1
    query = {}
    if race_id:
        query['race_id'] = race_id

    if role.label != 'admin':
        if identity == 'student':
            query['sids'] = account
        if identity == 'teacher':
            query['tid'] = account
    res = engine.find(Course, query)
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': [d.model_dump() for d in res]}


@course.route('/api/course', methods=['GET'])
def get_course_detail():
    course_id = request.args.get('course_id')  # ?course_id=1
    obj = engine.find_by_id(Course, int(course_id))
    res = obj.model_dump()
    res['students'] = [engine.find_by_id(Student, sid).model_dump() for sid in res['sids']]
    res['teacher'] = engine.find_by_id(Teacher, res['tid']).model_dump()
    return res


@course.route('/api/course/add', methods=['POST'])
def add_course():
    obj = Course(**request.get_json())
    engine.create(Course, obj)
    return {'code': 200, 'msg': 'success'}


@course.route('/api/course/delete', methods=['DELETE'])
def delete_course():
    d = request.get_json()
    for oid in d:
        engine.delete(Course, oid)
    return {'code': 200, 'msg': 'success'}


@course.route('/api/course/update', methods=['PUT'])
def update_course():
    obj = Course(**request.get_json())
    engine.update(Course, obj)
    return {'code': 200, 'msg': 'success'}
