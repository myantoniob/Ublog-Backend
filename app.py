import dtos
from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = []
publications = []

users.append(dtos.User("juan", "M", "jr","j@j.com","456"))
users.append(dtos.User("melvin", "M", "mel","m@m.com","789"))


def password_validar(password):
    numeros = ["0","1", "2", "3","4","5","6","7","8","9"]
    simbolos = ["/","*","-","+",".","_","@","|","#","$","%","&","(",")","=","?","¿","!","¡","{","[","}","]","^"]
    tengo_num = False
    tengo_sim = False
    if len(password) > 7:
        for hi in password:
                for num in numeros:
                    if hi == num:
                        tengo_num = True
                for sim in simbolos:
                    if hi == sim:
                        tengo_sim = True
    if tengo_num and tengo_sim:
        return True
    else:
        return False


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
            return jsonify({"nick": "nickname repeated"}), 401

    if password_validar(password):
        users.append(dtos.User(name, gender, nickname, email, password))
        return jsonify(request.get_json()), 200
    else:
        return jsonify({"message": "weak password"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data["nickname"]
    password = data["password"]
    for user in users:
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
                return jsonify({"usuario": "usuario existente"}), 400
    return jsonify({"message": "user not found"}), 400


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
        if user.nickname == cnickname:
            user.name = name
            user.gender = gender
            user.email = email
            if password_validar(password):
                user.password = password
            else:
                return jsonify({"passd": "weak password"})
        
            if user.nickname == nickname:
                user.nickname = nickname
                return jsonify(request.get_json())
            else:
                for us in users:
                    if us.nickname == nickname:
                        return jsonify({"user":"user repetido"})
                    else:
                        user.nickname = nickname
                        return jsonify(request.get_json())    
        else:
            return jsonify({"not": "No esta logeado"})
    

@app.route("/release", methods=["GET" ,"POST"])
def release():
    if request.method == "GET":
        temporal = []
        for publication in publications:
            temporal.append({
                "type": publication.type,
                "url": publication.url,
                "date": publication.date,
                "category": publication.category
            })

        return jsonify(temporal)

    elif request.method == "POST":
        data = request.get_json()
        nickname = data["nickname"]
        type = data["type"]
        url = data["url"]
        date = data["date"]
        category = data["category"]

        for user in users:
            if user.nickname == nickname:
                user.user_post.append(dtos.Publication(type, url, date, category))
                publications.append(dtos.Publication(type, url, date, category))
                return jsonify(request.get_json())

@app.route("/myRelease", methods=["GET", "POST"])
def myRelease():
    if request.method == "POST":
        data = request.get_json()
        nickname = data["nickname"]
        temporal = []
        for user in users:
            if user.nickname == nickname:
                for publication in user.user_post:
                    temporal.append({
                    "type": publication.type,
                    "url": publication.url,
                    "date": publication.date,
                    "category": publication.category
                    })
                return jsonify(temporal)
