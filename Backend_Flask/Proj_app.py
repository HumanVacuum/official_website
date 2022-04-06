from flask import Flask,render_template  # 渲染模板

app = Flask(__name__)

@app.route("/Projjudge")  # 判断语句
def control():
    context = {
            "concentration": 10, #PM2.5
            "TVOC":0.2
    }
    return render_template("Projjudge.html", **context)

if __name__ == '__main__':
    app.run()