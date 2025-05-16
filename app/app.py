from flask import Flask, request, url_for, redirect, render_template
from flask_login import LoginManager, login_required, login_user, logout_user
from db import db
from models import *
import os
import json
import hashlib
from blueprints.auth.auth_blueprint import auth_bp
from blueprints.user.user_blueprint import user_blueprint
from blueprints.pred.pred_blueprint import pred_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fidelizaAI.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
lm = LoginManager(app)
lm.login_view = 'auth.login'
lm.init_app(app)
app.secret_key = 'supersecretkey'
db.init_app(app)


app.register_blueprint(auth_bp)
app.register_blueprint(user_blueprint)
app.register_blueprint(pred_bp)

@lm.user_loader
def load_user(id):
    user = db.session.query(User).filter_by(id=id).first()
    return user

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)