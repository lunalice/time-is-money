from flask import Flask, render_template, jsonify, request, make_response, send_from_directory
from .database import init_db, db
from .models import User
from random import *
from IPython import embed
from . import utils
from .view_object.result_view_object import ResultViewObject
import os

def create_app():
    app = Flask(__name__,
                        static_folder='../../frontend/dist/static',
                                template_folder='../../frontend/dist')
    app.config.from_object('config.Config')
    init_db(app)

    return app

app = create_app()

# @app.route('/service-worker.js')
# def sw():
#     response = make_response(send_from_directory(app.template_folder + '/static', filename='service-worker.js'))
#     #change the content header file
#     response.headers['Content-Type']='application/javascript'
#     return response

@app.route('/api/users', methods=['POST'])
def post_user():
    payload = request.form
    result = ResultViewObject(payload.get('age'), int(payload.get('annual_income')) * utils.TEN_THOUSAND, \
        payload.get('working_hours'), payload.get('overtime'), payload.get('commuting_time'), payload.get('rent'))

    user = User(age=result.age, annual_income=result.annual_income, \
        working_hours=result.working_hours, overtime=result.overtime,  \
        commuting_time=result.commuting_time, rent=result.rent, holiday=result.holiday)
    db.session.add(user)
    db.session.commit()

    return jsonify(result.output()), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.order_by(User.created_at.desc()).all()
    result = []
    for user in users:
        result.append(ResultViewObject(user.age, user.annual_income,\
            user.working_hours, user.overtime, user.commuting_time, user.rent, holiday=user.holiday).output())

    return jsonify(result), 200

# 平均ページいつか作る・・・？
# @app.route('/api/users/average', methods=['GET'])
# def get_users():
#     users = User.query.order_by(User.created_at.desc()).limit(10).all()
#     result = []
#     for user in users:
#         result.append(view_object.ResultViewObject(user.age, user.annual_income,\
#             user.working_hours, user.overtime, user.commuting_time, user.rent, holiday=user.holiday).output())

#     return jsonify(result), 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
