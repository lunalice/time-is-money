from flask import Flask, render_template, jsonify, request
from application.database import init_db, db
from application.models import User
from random import *
from IPython import embed
import application.utils as Utils

def create_app():
    app = Flask(__name__,
                        static_folder='../../frontend/dist/static',
                                template_folder='../../frontend/dist')

    app.config.from_object('config.Config')
    init_db(app)

    return app

app = create_app()

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

# 登録
@app.route('/api/users', methods=['POST'])
def post_user():
    # jsonリクエストから値取得
    payload = request.form
    age = payload.get('age')
    annual_income = payload.get('annual_income')
    working_hours = payload.get('working_hours')
    overtime = payload.get('overtime')
    commuting_time = payload.get('commuting_time')
    rent = payload.get('rent')
    holiday = Utils.holiday()

    # レコードの登録 新規作成したオブジェクトをaddしてcommit
    user = User(age=age, annual_income=annual_income, working_hours=working_hours, overtime=overtime, commuting_time=commuting_time, rent=rent, holiday=holiday)
    db.session.add(user)
    db.session.commit()

    # response = jsonify(user.to_dict())
    # # レスポンスヘッダ設定
    # response.headers['Location'] = '/api/users/%d' % user.id
    # # HTTPステータスを200以外で返却したい場合
    return {}, 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
