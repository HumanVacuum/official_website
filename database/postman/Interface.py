from flask import Flask, render_template, request, make_response
from flask_cors import *

app = Flask(__name__)

@app.route('/')
def get_data():
    """
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
    header('Access-Control-Allow-Headers: Origin, Content-Type, X-Auth-Token');

    response = make_response(render_template("Interface.html"))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PATCH, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Origin, Content-Type, X-Auth-Token"
"""
    return render_template("Interface.html")

if __name__ == '__main__':
    app.run(debug = True)