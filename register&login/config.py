# coding=gbk

# �������ݿ��������Ϣ
# ���ݿ����ڷ�������ip��ַ
HOSTNAME = '127.0.0.1'
# �˿ںţ�Ĭ�϶�Ϊ3306
PORT = '3306'
# ���ݿ������,�ƺ�ֻ��Сд
# loginmessage
DATABASE = 'loginm'
# ���ݿ��û���������
USERNAME = 'root'
PASSWORD = '0000'
# �����涫���ϲ���һ���ַ����У����ż�Ϊ�Ϸ�Ҫ����Ķ�����charset=utf8��ʾ��utf8�ķ�ʽ���б���
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
# �����ݿ����ӵĲ�������app������һ����SQLALCHEMY_DATABASE_URI���������ע�ⲻ��URL
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_COMMIT_TEARDOWN = True

SECRET_KEY = "adssadas1237123123"

# ��������
# ��д�����ַ,��ȡѧУ����˿ںŵȶ���
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
# �Ƿ���Debugģʽ��������־��Ϣ����ʽ����ǵù�
MAIL_DEBUG = True
# ��Ҫȥqq���������ô��뷢���ʼ�
MAIL_USERNAME = "1528045870@qq.com"
MAIL_PASSWORD = "dsgjavszcvcsjega"
MAIL_DEFAULT_SENDER = "1528045870@qq.com"
