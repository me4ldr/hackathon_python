from model import *

student_list = [
    {'sid': '001', 'name': 'StudentA', 'password': '123', 'role_id': 3},
    {'sid': '002', 'name': 'StudentB', 'password': '123', 'role_id': 3},
    {'sid': '003', 'name': 'StudentC', 'password': '123', 'role_id': 3},
]
teacher_list = [
    {'tid': 'admin', 'name': 'Admin', 'password': '123', 'role_id': 1},
    {'tid': '001', 'name': 'TeacherA', 'password': '123', 'role_id': 2}
]
race_list = [
    {'race_id': 1, 'title': 'ModulaA', 'progress': 50, 'startdate': '2023/09/20', 'enddate':'2023/12/20'},
    {'race_id': 2, 'title': 'ModulaB', 'progress': 100, 'startdate': '2023/01/10', 'enddate':'2023/6/20'},
    {'race_id': 3, 'title': 'ModulaC', 'progress': 80, 'startdate': '2023/08/10', 'enddate':'2023/10/30'}
]
course_list = [
    {'course_id': 1, 'race_id': 1, 'name': 'CourseA', 'lessons': [{'name': 'L1', 'lesson_date': "2023-10-01"}],
     'tid': '001', 'sids': ['001']}
]
record_list = []
article_list = [
    {'articleId': 1, 'articleTitle': 'discussionA', 'articleContent': 'content',
     'articleTopics': ['Algorithm', 'Machine Learning'], 'userName': 'teacherA',
     'articleComments': [
         {'articleComment': 'hello world', 'userType': 'teacher', 'userName': 'Admin'}
     ]}
]
role_list = [
    {'role_id': 1, 'label': 'admin',
     'permissions': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]},
    {'role_id': 2, 'label': 'teacher',
     'permissions': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]},
    {'role_id': 3, 'label': 'student',
     'permissions': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]}
]
permission_list = [
    {'pid': 1, 'label': 'add user', 'action': 'add', 'type': 'user'},
    {'pid': 2, 'label': 'delete user', 'action': 'delete', 'type': 'user'},
    {'pid': 3, 'label': 'update user', 'action': 'update', 'type': 'user'},
    {'pid': 4, 'label': 'query user', 'action': 'query', 'type': 'user'},
    {'pid': 5, 'label': 'add race', 'action': 'add', 'type': 'race'},
    {'pid': 6, 'label': 'delete race', 'action': 'delete', 'type': 'race'},
    {'pid': 7, 'label': 'update race', 'action': 'update', 'type': 'race'},
    {'pid': 8, 'label': 'import user', 'action': 'import', 'type': 'user'},
    {'pid': 9, 'label': 'query race', 'action': 'query', 'type': 'race'},
    {'pid': 10, 'label': 'add record', 'action': 'add', 'type': 'record'},
    {'pid': 11, 'label': 'update record', 'action': 'update', 'type': 'record'},
    {'pid': 12, 'label': 'query record', 'action': 'query', 'type': 'record'},
    {'pid': 13, 'label': 'delete record', 'action': 'delete', 'type': 'record'},
    {'pid': 14, 'label': 'add role', 'action': 'add', 'type': 'role'},
    {'pid': 15, 'label': 'delete role', 'action': 'delete', 'type': 'role'},
    {'pid': 16, 'label': 'update role', 'action': 'update', 'type': 'role'},
    {'pid': 17, 'label': 'query role', 'action': 'query', 'type': 'role'},
    {'pid': 18, 'label': 'add permission', 'action': 'add', 'type': 'permission'},
    {'pid': 19, 'label': 'delete permission', 'action': 'delete', 'type': 'permission'},
    {'pid': 20, 'label': 'query permission', 'action': 'query', 'type': 'permission'},
    {'pid': 21, 'label': 'update permission', 'action': 'update', 'type': 'permission'},
    {'pid': 22, 'label': 'export user', 'action': 'export', 'type': 'user'},
    {'pid': 23, 'label': 'export record', 'action': 'export', 'type': 'record'},
    {'pid': 24, 'label': 'export race', 'action': 'export', 'type': 'race'},
    {'pid': 25, 'label': 'ai teacher', 'action': 'teacher', 'type': 'ai'}
]

students = {d['sid']: Student(**d) for d in student_list}
teachers = {d['tid']: Teacher(**d) for d in teacher_list}
races = {d['race_id']: Race(**d) for d in race_list}
courses = {d['course_id']: Course(**d) for d in course_list}
records = {d['record_id']: Record(**d) for d in record_list}
articles = {d['articleId']: Article(**d) for d in article_list}
roles = {d['role_id']: Role(**d) for d in role_list}
permissions = {d['pid']: Permission(**d) for d in permission_list}


def get_user_model(identity):
    return {'teacher': Teacher, 'student': Student}.get(identity)


def in_query(value, target):
    return value in target if type(target) is list else value == target


class Engine:
    repo_map = {
        Student: students,
        Teacher: teachers,
        Race: races,
        Course: courses,
        Record: records,
        Article: articles,
        Role: roles,
        Permission: permissions,
    }

    pk_map = {
        Student: 'sid',
        Teacher: 'tid',
        Race: 'race_id',
        Course: 'course_id',
        Record: 'record_id',
        Article: ' article_id',
        Role: 'role_id',
        Permission: 'pid',
    }

    def find(self, model, query=None):
        if query is None:
            query = {}
        repo = self.repo_map.get(model)
        res = [d for d in repo.values() if all([in_query(v, getattr(d, k)) for k, v in query.items()])]
        return res

    def find_one(self, model, query):
        res = self.find(model, query)
        return res[0] if res else None

    def find_by_id(self, model, oid):
        repo = self.repo_map.get(model)
        return repo.get(oid)

    def create(self, model, obj, oid=None):
        repo = self.repo_map.get(model)
        pk = self.pk_map.get(model)
        if not oid:
            oid = self.generate_oid(repo)
        setattr(obj, pk, oid)
        repo[oid] = obj

    def update(self, model, obj):
        repo = self.repo_map.get(model)
        pk = self.pk_map.get(model)
        res = self.find_one(model, {pk: getattr(obj, pk)})
        if res:
            repo[getattr(obj, pk)] = obj

    def delete(self, model, oid):
        repo = self.repo_map[model]
        repo.pop(oid)

    @staticmethod
    def generate_oid(repo):
        return max(repo.keys()) + 1
