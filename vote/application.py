from vote import app
from vote.db import *
from flask import (
    url_for,
    render_template,
    request,
    Response
)
from vote.config import *
from werkzeug.utils import secure_filename
import os
import datetime
import json

@app.route('/')
def main():
    candidate_list = []
    time = int(datetime.datetime.now().strftime("%Y%m%d%H%M"))
    reg = True if Config.REGISTER_PERIOD[0] <= time and time <= Config.REGISTER_PERIOD[1] else False
    opened = True if Config.RESULT_OPEN <= time else False
    count = db.session.query(Candidate).count()
    for i in range (1, count+1):
        query = db.session.query(Candidate).filter(Candidate.id.like(str(i)))
        candidate = eval(str(query.one()))
        candidate_list.append(candidate)
    return render_template('main.html', vote_title=Config.VOTE_TITLE, candidates=candidate_list, register=reg, opened=opened)

@app.route('/candidate/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', vote_title=Config.VOTE_TITLE, type_list = Config.PART_LIST)
    name = request.form.get('name')
    part = request.form.get('part')
    phrase = request.form.get('phrase')
    if (request.form.get('key') != Config.CANDIDATE_KEY):
        return '<script>alert("후보자 확인 코드를 확인하세요");history.go(-1)</script>'
    img = request.files['image']
    img_path = os.path.join('vote/static/candidate_img', img.filename)
    img.save(img_path)
    newCan = Candidate(
        name = name,
        part = part,
        phrase = phrase,
        image = img.filename
    )
    db.session.add(newCan)
    db.session.commit()
    return '<script>alert("후보자 등록을 성공했습니다.");history.go(-2);</script>'

@app.route('/vote', methods=['POST'])
def vote():
    data = request.data.decode('utf-8')
    data = json.loads(data)
    u_key = data['key']
    c_part = data['part']
    c_name = data['value']
    q_voter = db.session.query(Voter.query.filter(Voter.key == u_key).exists()).scalar()
    q_log = db.session.query(Log.query.filter(Log.user_key == u_key and Log.part == c_part).exists()).scalar()
    if (q_voter and q_log) or (not q_voter):
        return Response(status=400)
    newLog = Log(
        user_key=u_key, 
        part = c_part,
        value = c_name
    )
    db.session.add(newLog)
    db.session.commit()
    return 'ok'

@app.route('/dashboard')
def dashboard():
    return 'nop'