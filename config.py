from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO

app = Flask(__name__)
db = MongoEngine(app)
app.config['SECRET_KEY'] = '8KDJFAFDASF;AJLKASJFA;889df9das87&&&**98^^^^%^&**^%^&&(YHKJHggtuytyuh'
app.config['MONGODB_SETTINGS'] = {
    'db': 'my_chat',
    'host': '192.168.1.35',
    'port': 12345
}
bcrypt = Bcrypt(app)
socket = SocketIO(app)
