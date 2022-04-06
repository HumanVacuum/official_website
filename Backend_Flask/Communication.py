from flask import Flask, render_template, request


app = Flask(__name__)
global student
global admin
student = False
admin = False


def send_data(data, url, html_name):
    @app.route(url)
    def reader():
        return render_template(html_name, data_dict = data)

def receive_data(data, url):
    @app.route(url, methods = ['GET'])
    def writer():
        if request.form.get('name') == 'admin' and request.form.get('password') == '123':
            admin = True
            return ('admin_login.html')
        if request.form.get('name') == 'student' and request.form.get('password') == '1234':
            student = True
            return ('student_login.html')


@app.route('/display')
def show():
    list = []
    for i in range(1, 100):
        list[i] = i
    send_data(data = list, url = '/display', html_name = 'display.html')
