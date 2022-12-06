from config import db
from datetime import datetime

class Property(db.EmbeddedDocument):
    title = db.StringField()
    description = db.StringField()
    image = db.ImageField()
    date = db.DateTimeField(default=datetime.now())
    price = db.DecimalField()
    user_id = db.ReferenceField("ChatUser")
    tags = db.ListField()
    def __str__(self):
        return self.title

class ChatUser(db.Document):
    username = db.StringField()
    email = db.EmailField()
    telephone_number = db.StringField()
    password = db.StringField()
    is_login = db.BooleanField(default=False)
    last_login = db.DateTimeField(default=datetime.now())
    properties = db.EmbeddedDocumentListField("Property")

    def __str__(self):
        return self.username

