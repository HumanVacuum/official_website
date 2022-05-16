# 存放可能会导致循环引用的东西
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
# 创建Mail对象
mail = Mail()
