from datetime import datetime
from application.database import db
from application import app
from IPython import embed
from flask import Flask

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    annual_income = db.Column(db.Integer, nullable=False)
    holiday = db.Column(db.Integer, nullable=False)
    working_hours = db.Column(db.Integer, nullable=False)
    overtime = db.Column(db.Integer, nullable=False)
    commuting_time = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    
    # @property
    # def serialize(self):
    #     return {
    #         'id': self.id,
    #         'age': self.age,
    #         'annual_income': self.annual_income,
    #         'holiday': self.holiday,
    #         'working_hours': self.working_hours,
    #         'overtime': self.overtime,
    #         'commuting_time': self.commuting_time,
    #         'rent': self.rent,
    #         'created_at': self.created_at,
    #         'updated_at': self.updated_at,
    #     }
