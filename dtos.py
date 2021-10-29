class User:
    def __init__(self, name, gender,nickname, email, password):
        self.name = name
        self.gender = gender
        self.nickname = nickname
        self.email = email
        self.password = password
        

class Publication:
    def __init__(self, type, url, date, category):
        self.type = type
        self.url = url
        self.date = date
        self.category = category