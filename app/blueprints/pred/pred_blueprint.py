from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from models import *
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from db import db
from werkzeug.utils import secure_filename
from docling.document_converter import DocumentConverter
import os
from datetime import datetime

pred_bp = Blueprint('pred', __name__, template_folder='templates', url_prefix='/pred')

ALLOWED_EXTENSIONS = set(['csv'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@pred_bp.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return 'error'
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return "weee"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f'{filename.rsplit(".", 1)[0]}_{timestamp}.csv'

            file_path = os.path.join('app/static/uploads', new_filename)
            file.save(file_path)

            uploadDoc = Documento(
                user_id=current_user.id,
                caminho=file_path,
                nome_doc=new_filename
            )
            db.session.add(uploadDoc)
            db.session.commit()
            flash('Sucesso')
            return 'uploaded' # if not ALLOWED_EXTENSIONS, return 'error'
        return 'error'
    #GET
    return render_template('upload.html')