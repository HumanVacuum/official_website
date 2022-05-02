from flask import Flask, session, g
import config
from exts import db, mail
# 导入两个模块
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
# 注册下qa&user
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)


# 钩子函数，在请求发出前执行
@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g绑定一个叫做user的变量，他的值是user这个变量,g是全局变量
            # setattr(g,"user",user)
            g.user = user
        except:
            g.user = None


# 上下文处理器(渲染的所有代码都会去执行)

@app.context_processor
def context_processor():
    # 在当前用户登录的情况下返回
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}


# 请求来了 ->before_request ->视图函数 ->视图函数中返回模板 -> context_processor
if __name__ == '__main__':
    app.run()
