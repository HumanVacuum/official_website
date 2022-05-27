from flask import Blueprint, render_template, g

# display
bp = Blueprint("dp", __name__, url_prefix="/")


@bp.route("/")
def index():
    # todo: have changed
    return render_template("homepage.html")


# admin/setting page
@bp.route('/user', methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")


# present data page
@bp.route('/user/present', methods=['GET', 'POST'])
def present():
    return render_template("present.html")


# history data op1
@bp.route('/user/history/day', methods=['GET', 'POST'])
def history_op1():
    return render_template("history_day.html")


# history data op2
@bp.route('/user/history/dynamic', methods=['GET', 'POST'])
def history_op2():
    return render_template("history_dynamic.html")


# console page
@bp.route('/user/console', methods=['GET', 'POST'])
def console():
    return render_template("console.html")
