from flask import Blueprint, render_template

module = Blueprint("index", "index", url_prefix="/", template_folder="templates")


@module.route("/")
def index():
    return render_template("index.html")
