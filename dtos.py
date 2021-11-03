class User:
    
    def __init__(self, name, gender,nickname, email, password):
        self.name = name
        self.gender = gender
        self.nickname = nickname
        self.email = email
        self.password = password
        self.user_post = []            
        

class Publication:
    def __init__(self, type, url, date, category, nickname, id):
        self.type = type
        self.url = url
        self.date = date
        self.category = category
        self.nickname = nickname
        self.cantidad = 0
        self.id = id