from flask import Blueprint,render_template,g

bp = Blueprint("nonuser", __name__, url_prefix="/")


@bp.route("/")
def index():
    # todo: have changed
    return render_template("homepage.html")
