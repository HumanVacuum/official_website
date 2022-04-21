import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库信息
db_config = {
    'host': 'localhost',
    'port': '3306',
    'database': 'bdpoi',
    'username': 'bdpoi',
    'password': 'rKADFaJxAG2b7Lfd'
}
app.config['SECRET_KEY'] = 'hard to guess'

# url的格式为,数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://{username}:{password}@{host}:{port}/{database}'.format(**db_config)
# 动态追踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)

# 声明模型类
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class Poi(db.Model):
    __tablename__ = "po_poi"
    poi_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    poi_name = db.Column(db.String(255), nullable=False)
    poi_category_id = db.Column(db.Integer, nullable=False)

def index():
    # 查询数据库
    results = User.query.all()
    # 定义字典和序列
    rows = []
    data = {}
    for rs in results:
        row = {"id": rs.id, "name": rs.name}
        rows.append(row)
    data['code'] = 0
    data['msg'] = 'OK'
    data['data'] = rows

    # 输出标准的JSON字符串
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

# 获取数据库记录API接口
def get_poi(pid=None):
    if pid is None:
        results = Poi.query.all()
    else:
        results = Poi.query.filter_by(poi_id=pid).all()

    # 定义字典和序列
    rows = []
    data = {}
    for rs in results:
        row = {"poi_id": rs.poi_id, "poi_name": rs.poi_name, "poi_category_id": rs.poi_category_id}
        rows.append(row)
    data['code'] = 0
    data['msg'] = 'OK'
    data['data'] = rows

    # 输出标准的JSON字符串
    json_str = json.dumps(data, ensure_ascii=False)
    return json_str

if __name__ == '__main__':
    app.run()


