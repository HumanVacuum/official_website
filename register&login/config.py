# coding=gbk

# 这是数据库的配置信息
# 数据库所在服务器的ip地址
HOSTNAME = '127.0.0.1'
# 端口号，默认都为3306
PORT = '3306'
# 数据库的名字,似乎只能小写
# loginmessage
DATABASE = 'loginm'
# 数据库用户名和密码
USERNAME = 'root'
PASSWORD = '0000'
# 把上面东西合并到一个字符串中，括号即为上方要放入的东西，charset=utf8表示用utf8的方式进行编码
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# 将数据库连接的参数传给app，设置一个‘SQLALCHEMY_DATABASE_URI’的配置项，注意不是URL
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = "adssadas1237123123"

# 邮箱配置
# 填写邮箱地址,获取学校邮箱端口号等东西
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# 是否开启Debug模式，开启日志信息，正式部署记得关
MAIL_DEBUG = True
# 需要去qq邮箱设置让代码发送邮件
MAIL_USERNAME = "1528045870@qq.com"
MAIL_PASSWORD = "dsgjavszcvcsjega"
MAIL_DEFAULT_SENDER = "1528045870@qq.com"
