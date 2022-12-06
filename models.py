from config import db

class ChatUser(db.Document):
    username = db.StringField()
    email = db.EmailField()
    telephone_number = db.StringField()
    password = db.StringField()
    is_login = db.BooleanField(default=False)
