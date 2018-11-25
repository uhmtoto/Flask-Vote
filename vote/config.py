import os

class Config:
    VOTE_TITLE = '제 1회 회장 선거'
    CANDIDATE_KEY = 'pw'
    PART_LIST = ['정회장', '부회장']
    REGISTER_PERIOD = [20181101, 20181130]

class SQLConf:
    SECRET_KEY = os.urandom(24)
    DATABASE_URI = 'sqlite:///app.db'
    TRACK_MODIFICATIONS = False