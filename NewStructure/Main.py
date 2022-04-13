from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)


# homepage
@app.route('/', methods=['GET', "POST"])
def root():
    if request.method == 'GET':
        return render_template('HomePage.html')


# admin sign up page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("Login.html")


# admin page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template("Admin.html")

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
