from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', "POST"])
def root():
    if request.method == 'GET':
        return render_template('Login.html')
    if request.method == 'POST':
        password = request.form.get('code')
        if password == '1234':
            return redirect(url_for('admin'))
        if password == '123':
            return redirect(url_for('user'))


@app.route('/Admin', methods = ['GET','POST'])
def admin():
    return render_template('Admin.html')

@app.route('/User', methods = ['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('User.html')
    if request.method == 'POST':
        return redirect(url_for('personal'))

@app.route('/User/Account')
def personal():
    return render_template("Account.html")

@app.route('/SignUpUser')
def signUpUser():
    return render_template("SignUpUser.html")

@app.route('/SignUpAdmin')
def signUpAdmin():
    return render_template("SignUpAdmin.html")

@app.route('/Admin/Console')
def console():
    return render_template("Console.html")

@app.route('/Admin/DataZone')
def dataZone():
    return render_template("DataZone.html")

@app.route('/Admin/DataHistory')
def dataHistory():
    return render_template("DataHistory.html")

@app.route('/Admin/DataPresent')
def dataPresent():
    return render_template("DataPresent.html")



if __name__ == '__main__':
    app.run()