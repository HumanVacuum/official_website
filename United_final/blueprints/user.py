from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    session,
    flash
)
from exts import mail, db
from flask_mail import Message
from models import EmailCaptchaModel, UserModel
import string
import random
from datetime import datetime
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("user", __name__, url_prefix="/admin")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            # 需要将相应密码的加密形态进行匹配
            if user and check_password_hash(user.password, password):
                # 将用户id存至session
                session['user_id'] = user.id
                # 登录成功后跳转
                # todo modify url
                return redirect("/admin/present")
            else:
                # 错误信息弹窗
                flash("邮箱和密码不匹配")
                return redirect(url_for("user.login"))
        else:
            flash("邮箱或密码格式错误！")
            return redirect(url_for("user.login"))


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            # 在forms中进行验证码判断
            email = form.email.data
            # username = form.username.data
            password = form.password.data

            # 加密 md5哈希成密文 无法逆向，存储md5
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))


# 验证码存储位置 memcached/redis/数据库中 前两个是在内存中，可以过期，但比较难，此次存在数据库中

# 退出登录
@bp.route("/logout")
def logout():
    # 清除session中所有的数据
    session.clear()
    # todo 修改地址，导航到主页
    return redirect(url_for('user.login'))


# 测试下能否发送邮件
@bp.route("/captcha", methods=['POST'])
def get_captcha():
    # 用户输入邮箱 GET法
    email = request.form.get("email")
    # 验证码从大写字母，小写字母，数字中随机取四位
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 4))
    # 定义一个message
    if email:
        message = Message(
            subject="邮箱测试",
            recipients=[email],
            body=f"【人体吸尘】 您的注册验证码是：{captcha}"
            # html和body设置一个就行了，如果有富文本图片可用html
        )
        mail.send(message)
        # 判断这个邮箱是否已经存储了验证码
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        # 如果有就修改一下验证码
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now()
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        print("captcha:", captcha)
        # 发现200的请求，即为成功
        return jsonify({"code": 200})
    else:
        # code: 400，客户端错误
        return jsonify({"code": 400, "message": "请先传递邮箱！"})
