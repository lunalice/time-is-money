from flask import Flask, render_template, jsonify, request
from application.database import init_db, db
from application.models import User
from random import *
from IPython import embed
import application.utils as Utils
import application.view_object.result_view_object as view_object

def create_app():
    app = Flask(__name__,
                        static_folder='../../frontend/dist/static',
                                template_folder='../../frontend/dist')
    app.config.from_object('config.Config')
    init_db(app)

    return app

app = create_app()

# sample
@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/users', methods=['POST'])
def post_user():
    payload = request.form
    result = view_object.ResultViewObject(payload.get('age'), int(payload.get('annual_income')) * Utils.TEN_THOUSAND, \
        payload.get('working_hours'), payload.get('overtime'), payload.get('commuting_time'), payload.get('rent'))

    user = User(age=result.age, annual_income=result.annual_income, \
        working_hours=result.working_hours, overtime=result.overtime,  \
        commuting_time=result.commuting_time, rent=result.rent, holiday=result.holiday)
    db.session.add(user)
    db.session.commit()

    return jsonify(result.output()), 200

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append(view_object.ResultViewObject(user.age, user.annual_income,\
            user.working_hours, user.overtime, user.commuting_time, user.rent, holiday=user.holiday).output())
    
    return jsonify(result), 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
