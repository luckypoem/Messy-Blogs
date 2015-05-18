# coding: utf-8
from datetime import datetime
from ._base import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('user_post',
            lazy='dynamic',
            order_by='desc(Post.created_at)'))

    def __setattr__(self, name, value):
        super(Post, self).__setattr__(name, value)


    def __repr__(self):
        return '<Post %s>' % self.title
