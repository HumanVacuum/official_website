from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask import session, g
import config
from exts import db, mail
from blueprints import qa_bp
from blueprints import user_bp
from flask_migrate import Migrate
from models import UserModel

app = Flask(__name__)

# 进行config绑定
app.config.from_object(config)

# 初始化app，创建各类对象
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)

# 注册qa&user
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)
# confirm login status
# 钩子函数，在请求发出前执行


@app.before_request
def before_request():
    user_id = session.get("user_id")
    if request.path == "/":
        return None
    if request.path == "/admin/login":
        return None
    if request.path == "/admin/register":
        return None
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个叫做user的变量，他的值是user这个变量,g是全局变量
            # setattr(g,"user",user)
            g.user = user
        except:
            g.user = None
        return None
    # todo 改成未登录状态提醒页面
    return render_template("login.html")


# 上下文处理器(渲染的所有代码都会去执行)
@app.context_processor
def context_processor():
    # 在当前用户登录的情况下返回
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


# homepage
@app.route('/', methods=['GET', "POST"])
def root():
    if request.method == 'GET':
        return render_template('homepage.html')


# present data page
@app.route('/admin/present', methods=['GET', 'POST'])
def present():
    return render_template("present.html")


# history data op1
@app.route('/admin/history/option1', methods=['GET', 'POST'])
def history_op1():
    return render_template("historyOp1.html")


# history data op2
@app.route('/admin/history/option2', methods=['GET', 'POST'])
def history_op2():
    return render_template("historyOp2.html")


# console page
@app.route('/admin/console', methods=['GET', 'POST'])
def console():
    return render_template("console.html")


# admin/setting page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")


# 请求来了 ->before_request ->视图函数 ->视图函数中返回模板 -> context_processor
if __name__ == '__main__':
    app.run()
