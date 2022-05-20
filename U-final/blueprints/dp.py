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
@bp.route('/user/history/option1', methods=['GET', 'POST'])
def history_op1():
    return render_template("historyOp1.html")


# history data op2
@bp.route('/user/history/option2', methods=['GET', 'POST'])
def history_op2():
    return render_template("historyOp2.html")


# console page
@bp.route('/user/console', methods=['GET', 'POST'])
def console():
    return render_template("console.html")
