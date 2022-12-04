from config import app
from flask import request
from models import ChatUser as User
from config import bcrypt
import jwt

@app.route('/signup/', methods=['POST'])
def signup():
    try:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        telephone_number = request.json['tel']
        if User.objects.filter(username=username).first() or User.objects.filter(email=email).first()  or User.objects.filter(telephone_number=telephone_number).first():
            return {"status": "User already exists"}, 403
        User.objects.create(username=username, email=email, password=bcrypt.generate_password_hash(password), telephone_number=telephone_number)
        return {"status": "User account created"}, 201
    except Exception as e:
        return {"status": str(e)}, 500

@app.route('/login/', methods=["POST"])
def login():
    username = request.json.get("username")
    email = request.json.get('email')
    password = request.json.get('password')
    user = User.objects.filter(username=username).first() or User.objects.filter(email=email).first()
    if user:
        if bcrypt.check_password_hash(user.password, password):
            username = user.username
            token = jwt.encode({"username": username}, app.config['SECRET_KEY'])
            return {"status": token}, 200
        else:
            return {"status": "Invalid password specified"}, 401
    else:
        return {"status": "A user with specified account credentials does not exist"}, 404


app.run(debug=True)