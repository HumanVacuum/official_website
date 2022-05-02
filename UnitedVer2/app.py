from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from datetime import timedelta

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

# homepage
@app.route('/', methods=['GET', "POST"])
def root():
    if request.method == 'GET':
        return render_template('homepage.html')


# admin log in page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        return redirect(url_for('present'))


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

# present data page - get data
# @app.route('/getData', methods=['GET', 'POST'])
# def get_data():
#     if request.method == 'GET':
#         try:
#             # test text
#             return {"time": "2022.Apr.6, 14:00", "data": "30", "level": "无污染", "strategy": "无需防护"}
#         except Exception as e:
#             return str(e)


if __name__ == '__main__':
    app.run()
