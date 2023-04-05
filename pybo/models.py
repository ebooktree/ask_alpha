#데이터베이스를 관리하는 영역.
from pybo import db

# 똑똑 수정하면서 함수를 불러왔음.
from datetime import datetime


question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

""" class Search_Keyword_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    created_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
"""

class Search_Keyword_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    created_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    @staticmethod
    def get_keyword_list(category):
        if category == 'happy':
            return happy_list1 + happy_list
        elif category == 'sad':
            return sad_list1 + sad_list
        elif category == 'angry':
            return angry_list1 + angry_list
        elif category == 'hurt':
            return hurt_list1 + hurt_list
        elif category == 'power':
            return power_list1 + power_list
        elif category == 'shame':
            return shame_list1 + shame_list
        elif category == 'alone':
            return alone_list1 + alone_list
        else:
            return []

class Search_Result_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_keyword = db.Column(db.String(200), nullable=False)
    emotion = db.Column(db.String(200), nullable=False)
    color_name = db.Column(db.String(200), nullable=False)
    color_code = db.Column(db.String(200), nullable=False)
    book_title = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

