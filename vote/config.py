import os

class Config:
    VOTE_TITLE = '제 1회 회장 선거'
    CANDIDATE_KEY = 'pw'
    PART_LIST = ['정회장', '부회장']
    REGISTER_PERIOD = [201811010000, 201811300000]
    RESULT_OPEN = 201811050000

class SQLConf:
    SECRET_KEY = os.urandom(24)
    DATABASE_URI = 'sqlite:///app.db'
    TRACK_MODIFICATIONS = False