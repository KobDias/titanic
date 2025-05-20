from sqlalchemy import DateTime
from flask_login import UserMixin
from db import db

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)
    documents = db.relationship('Documento', backref='User')

class Documento(db.Model):
    __tablename__ = 'Documento'
    doc_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    caminhoOriginal = db.Column(db.String(200), nullable=False)
    caminhoPredito = db.Column(db.String(200), nullable=True)
    nome_doc = db.Column(db.String(100), nullable=False)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())
    views = db.relationship('View', backref='Documento')

class View(db.Model):
    view_id = db.Column(db.Integer, primary_key=True)
    doc_id = db.Column(db.Integer, db.ForeignKey('Documento.doc_id'), nullable=False)
    caminho_view = db.Column(db.String(200), nullable=False)
    # html_content = db.Column(db.Text, nullable=False)
    # view_name = db.Column(db.String(100), nullable=False)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())