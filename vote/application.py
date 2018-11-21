from vote import app
from flask import (
    url_for,
    render_template,
    request
)
from werkzeug.utils import secure_filename
import os

# Config
VOTE_TITLE = 'VOTE_TITLE'
CANDIDATE_KEY = 'SECRET_KEY'

@app.route('/')
def main():
    return render_template('main.html', vote_title=VOTE_TITLE)

@app.route('/candidate/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    name = request.get.form('name')
    part = request.get.form('part')
    phrase = request.get.form('phrase')
    if (request.get.form('key') != SECRET_KEY):
        return '개인 식별 코드를 확인하세요'
    image = request.files['image']
    image.save(os.path.join('static', secure_filename(image.filename)))
    # Register Process
    
    return '후보자 등록을 성공했습니다.'