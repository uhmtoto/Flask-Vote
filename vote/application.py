from vote import app
from vote.db import *
from flask import (
    url_for,
    render_template,
    request
)
from werkzeug.utils import secure_filename
import os, datetime

# Config Start
VOTE_TITLE = '제 1회 회장 선거'
CANDIDATE_KEY = 'pw'
PART_LIST = ['정회장', '부회장']
REGISTER_PERIOD = [20181101, 20181131]
# Config End

@app.route('/')
def main():
    date = int(datetime.datetime.now().strftime("%Y%m%d"))
    reg = True if REGISTER_PERIOD[0] <= date and date <= REGISTER_PERIOD[1] else False
    return render_template('main.html', vote_title=VOTE_TITLE, register=reg)

@app.route('/candidate/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', vote_title=VOTE_TITLE, type_list = PART_LIST)
    name = request.form.get('name')
    part = request.form.get('part')
    phrase = request.form.get('phrase')
    if (request.form.get('key') != CANDIDATE_KEY):
        return '<script>alert("개인 식별 코드를 확인하세요");</script>'
    image = request.files['image']
    image_path = os.path.join('candidate_img', image.filename)
    image.save(image_path)
    candidate = Candidate(name=name, part=part, phrase=phrase, image=image_path)
    db.session.add(candidate)
    db.session.commit()
    return '<script>alert("후보자 등록을 성공했습니다.");history.go(-1);</script>'