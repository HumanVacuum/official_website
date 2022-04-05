from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', "POST"])
def root():
    if request.method == 'GET':
        return render_template('login.html')
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

@app.route('/User/个人中心')
def personal():
    return render_template("个人中心.html")

if __name__ == '__main__':
    app.run()