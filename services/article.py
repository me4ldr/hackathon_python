from datetime import datetime

from flask import Blueprint, request

from mock_engine import Engine
from model import *
from utils.jwt_util import get_identity

article = Blueprint('article', __name__)

engine = Engine()


@article.route('/api/article/list', methods=['GET'])
def get_article_list():
    res = engine.find(Article)
    data = [r.model_dump(exclude='article_comments', by_alias=True) for r in res]
    return {'code': 200, 'msg': 'success', 'count': len(res), 'data': data}


@article.route('/api/article', methods=['GET'])
def get_article_detail():
    article_id = request.args.get('article_id')  # ?article_id=1
    obj = engine.find_by_id(Article, int(article_id))
    return {'code': 200, 'msg': 'success', 'data': obj.model_dump(by_alias=True)}


@article.route('/api/article', methods=['POST'])
def post_article_item():
    d = request.get_json()  # {'text': 'abc', 'article_id': 1}
    identity, account, _, name = get_identity(request.cookies)
    item = ArtileItem(userType=identity, userId=account, articleComment=d['articleComment'], userName=name)
    res = engine.find_by_id(Article, int(d['articleId']))
    res.article_comments.append(item)
    res.article_comment_count += 1
    return {'code': 200, 'msg': 'success'}
    # TODO ad GPT response for identity == 'student'?


@article.route('/api/topic', methods=['GET'])
def get_topic():
    res = engine.find(Article)
    topics = [t for a in res for t in a.article_topics]
    hot_topic = max(set(topics), key=topics.count)
    return {'code': 200, 'msg': 'success',
            'data': [{'topicName': hot_topic, 'articleNum': topics.count(hot_topic), 'topicDesc': 'hot topic', }]
            }
