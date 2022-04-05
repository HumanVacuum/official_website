#coding=gbk
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from threading import Timer
import time
import datetime
import random
app= Flask(__name__)
now_time = datetime.datetime.now()
max=0
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'ttttest'
USERNAME = 'root'
PASSWORD = '0000'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

#造车
db = SQLAlchemy(app)


class testNum(db.Model):
    __tablename__="testNUM"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time=db.Column(db.DateTime,nullable=False)
    PM=db.Column(db.Float,nullable=False)
db.create_all()

def newData():
    #添加数据
    x=1+0.1*random.randint(1,9)
    testNUM=testNum(time=now_time,PM=x)
    db.session.add(testNUM)
    #提交数据
    db.session.commit()
    return

def gotNew():
    newN=testNum.query.filter_by(id=max)[0]
    print(newN.PM)
    print(max)
    return

def loop_func(func,second):
    while True:
        func()
        time.sleep(second)

for i in range(1000):
    newData()
    max=max+1

loop_func(gotNew,1)


if __name__ =='__main__':
    app.run(debug=True)
