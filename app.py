import dtos
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []

@app.route('/index')
def index():
    return jsonify(), 200


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    name = data["name"]
    gender = data["gender"]
    nickname = data["nickname"]
    email = data["email"]
    password = data["password"]
    
    for user in users:
        if user.nickname == nickname:
            return jsonify({"message": "nickname repeated"}), 400
    users.append(dtos.User(name, gender, nickname, email, password))
    return jsonify(request.get_json()), 200


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data["nickname"]
    password = data["password"]
    for user in users:
        if user.nickname == nickname:
            if user.password == password:
                return jsonify({
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date": user.date,
                    "gender": user.gender,
                    "nickname": user.nickname,
                    "phone": user.phone
                }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    return jsonify({"message", "user not found"}), 400
