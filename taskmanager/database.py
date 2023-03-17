import os
from taskmanager import db

class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(30), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='category', cascade='all, delete', lazy=True)

    def __repr__(self):
        return self.category_name

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(40), nullable=False, unique=True)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, nullable=False, default=False)
    due_Date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
