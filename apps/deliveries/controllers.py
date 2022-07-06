from flask import Blueprint, render_template

deliveries = Blueprint("deliveries", __name__, url_prefix="/deliveries")


@deliveries.route("/")
def index():
    return render_template("index.html")
