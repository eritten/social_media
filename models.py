from config import db
from datetime import datetime

class ChatUser(db.Document):
    username = db.StringField()
    email = db.EmailField()
    telephone_number = db.StringField()
    password = db.StringField()
    is_login = db.BooleanField(default=False)
    last_login = db.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.username

    images = db.ReferenceField('Image')


class Image(db.EmbeddedDocument):
    url = db.URLField()
    property_id = db.ReferenceField('Property')



class Property(db.Document):
    title = db.StringField()
    description = db.StringField()
    image = db.EmbeddedDocumentListField('Image')

    date = db.DateTimeField(default=datetime.now())
    price = db.DecimalField()
    tags = db.ListField()
    def __str__(self):
        return self.title
