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
    candidate_list = []
    date = int(datetime.datetime.now().strftime("%Y%m%d"))
    reg = True if REGISTER_PERIOD[0] <= date and date <= REGISTER_PERIOD[1] else False
    count = db.session.query(Candidate).count()
    for i in range (1, count+1):
        query = db.session.query(Candidate).filter(Candidate.id.like(str(i)))
        candidate = str(query.one()).split('|')
        candidate_list.append(candidate)
    return render_template('main.html', vote_title=VOTE_TITLE, register=reg, candidates=candidate_list)

@app.route('/candidate/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', vote_title=VOTE_TITLE, type_list = PART_LIST)
    name = request.form.get('name')
    part = request.form.get('part')
    phrase = request.form.get('phrase')
    if (request.form.get('key') != CANDIDATE_KEY):
        return '<script>alert("후보자 확인 코드를 확인하세요");history.go(-1)</script>'
    img = request.files['image']
    img_path = os.path.join('vote/static/candidate_img', img.filename)
    img.save(img_path)
    candidate = Candidate(name=name, part=part, phrase=phrase, image=img.filename)
    db.session.add(candidate)
    db.session.commit()
    return '<script>alert("후보자 등록을 성공했습니다.");history.go(-2);</script>'