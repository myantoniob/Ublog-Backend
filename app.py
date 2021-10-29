import dtos
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
publications = []

users.append(dtos.User("juan", "M", "jr","j@j.com","456"))
users.append(dtos.User("melvin", "M", "mel","m@m.com","789"))

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
        print(nickname)
        print(users[0].nickname)
        print(user.nickname == nickname)
        print(user.password)
        print(password)
        if user.nickname == nickname:
            if user.password == password:
                return jsonify({
                    "name": user.name,
                    "gender": user.gender,
                    "nickname": user.nickname,
                    "email": user.email,
                    "password": user.password
                }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    return jsonify({"message", "user not found"}), 400

@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    cnickname = data["cnickname"]
    name = data["name"]
    gender = data["gender"]
    nickname = data["nickname"]
    email = data["email"]
    password = data["password"]
     
    for user in users:
        print(user.nickname == cnickname)
        if user.nickname == cnickname:
            user.name = name
            user.gender = gender
            user.nickname = nickname
            user.email = email
            user.password = password
            for si in users:
                
                print(si.nickname)
                print(si.password)
            return jsonify(request.get_json())
        else:
            return jsonify({"message": " interno usuario no existe"})
    return jsonify({"message": "usuario no existe"})



@app.route("/release", methods=["GET" ,"POST"])
def release():
    if request.method == "GET":
        return jsonify({
            "images": publications[0].type,
            "url": publications[0].url,
            "date": publications[0].date,
            "category": publications[0].category
        })

    elif request.method == "POST":
        data = request.get_json()
        type = data["images"]
        url = data["url"]
        date = data["date"]
        category = data["category"] 
        publications.append(dtos.Publication(type, url, date, category))
        return jsonify(request.get_json())