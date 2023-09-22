from datetime import date
from typing import Optional, List, Union

from pydantic import BaseModel, Field


class Student(BaseModel):
    sid: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    sex: Optional[int] = Field(default=None)
    grade: Optional[int] = Field(default=None)
    dclass: Optional[str] = Field(default=None, alias='class')
    role_id: Optional[int] = Field(default=None)


class Teacher(BaseModel):
    tid: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    rank: Optional[int] = Field(default=None)
    description: Optional[str] = Field(default=None)
    role_id: Optional[int] = Field(default=None)


class Race(BaseModel):
    race_id: Optional[int] = Field(default=None)
    title: Optional[str] = Field(default=None)
    sponsor: Optional[str] = Field(default=None)
    type: Optional[str] = Field(default=None)
    level: Optional[int] = Field(default=None)
    location: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    progress: Optional[int] = Field(default=None)
    startdate: Optional[str] = Field(default=None)
    enddate: Optional[str] = Field(default=None)


class Lesson(BaseModel):
    name: Optional[str] = Field(default=None)
    lesson_date: date = Field(default=None)


class Course(BaseModel):
    course_id: Optional[int] = Field(default=None)
    race_id: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    lessons: List[Lesson] = Field(default=[])
    tid: Optional[str] = Field(default=None)
    sids: List[str] = Field(default=[])


class Record(BaseModel):
    record_id: Optional[int] = Field(default=None)
    status: Optional[int] = Field(default=None)
    score: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    sid: Optional[str] = Field(default=None)
    tid: Optional[str] = Field(default=None)
    course_id: Optional[str] = Field(default=None)


class ArtileItem(BaseModel):
    article_comment: Optional[str] = Field(default=None, alias='articleComment')
    user_type: Optional[str] = Field(default=None, alias='userType')
    user_id: Optional[str] = Field(default=None, alias='userId')
    user_name: Optional[str] = Field(default=None, alias='userName')
    article_comment_time: Optional[date] = Field(default=None, alias='articleCommentTime')


class Article(BaseModel):
    article_id: Optional[int] = Field(default=None, alias='articleId')

    user_name: Optional[str] = Field(default=None, alias='userName')
    article_title: Optional[str] = Field(default=None, alias='articleTitle')
    article_content: Optional[str] = Field(default=None, alias='articleContent')
    article_topics: List[str] = Field(default=None, alias='articleTopics')

    article_view: Optional[str] = Field(default=None, alias='articleView')
    article_comment_count: Optional[str] = Field(default=0, alias='articleCommentCount')

    course_id: Optional[str] = Field(default=None)
    article_comments: List[ArtileItem] = Field(default=[], alias='articleComments')


class Permission(BaseModel):
    pid: Optional[int] = Field(default=None)
    label: Optional[str] = Field(default=None)
    action: Optional[str] = Field(default=None)  # 'add', 'delete', 'update', 'query', 'import', 'export'
    dtype: Optional[str] = Field(default=None, alias='type')  # 'user', 'role', 'race', 'record', 'permission'


class Role(BaseModel):
    role_id: Optional[int] = Field(default=None)
    label: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    permissions: List[Union[int, Permission]] = Field(default=[])
