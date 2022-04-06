from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)


# homepage
@app.route('/', methods=['GET', "POST"])
def root():
    if request.method == 'GET':
        return render_template('Login.html')
    if request.method == 'POST':
        password = request.form.get('code')
        if password == '1234':
            return redirect(url_for('admin'))
        if password == '123':
            return redirect(url_for('user'))


# sign up page - user
@app.route('/SignUpUser', methods=['GET', 'POST'])
def sign_up_user():
    if request.method == 'GET':
        return render_template("SignUpUser.html")
    if request.method == 'POST':
        return redirect(url_for('root'))


# sign up page - admin
@app.route('/SignUpAdmin', methods=['GET', 'POST'])
def sign_up_admin():
    if request.method == 'GET':
        return render_template("SignUpAdmin.html")
    if request.method == 'POST':
        return redirect(url_for('root'))



# sign in as administrator
@app.route('/Admin', methods=['GET', 'POST'])
def admin():
    return render_template('Admin.html')


# admin - present data
@app.route('/Admin/DataPresent')
def data_present():
    return render_template("DataPresent.html")


# admin - console
@app.route('/Admin/Console')
def console():
    return render_template("Console.html")


# admin - data zone
@app.route('/Admin/DataZone')
def data_zone():
    return render_template("DataZone.html")


# admin - data history
@app.route('/Admin/DataHistory')
def data_history():
    return render_template("DataHistory.html")


# sign in as user
@app.route('/User', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('User.html')
    if request.method == 'POST':
        return redirect(url_for('personal'))


# user - account
@app.route('/User/Account')
@app.route('/Admin/Account')
def personal():
    return render_template("Account.html")


# present data page - get data
@app.route('/getData', methods=['GET', 'POST'])
def get_data():
    if request.method == 'GET':
        try:
            # test text
            return {"time": "2022.Apr.6, 14:00", "data": "30", "level": "无污染", "strategy": "无需防护"}
        except Exception as e:
            return str(e)


if __name__ == '__main__':
    app.run()
