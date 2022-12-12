from flask import Blueprint, render_template, Response
from flask_login import login_required, current_user
from Recognition.streaming import gen

routes = Blueprint("routes", __name__)


@routes.route("/")
@login_required
def home():
    return render_template("index.html", user=current_user)


@routes.route("/attendance")
@login_required
def attendance():
    return render_template("attendance.html", user=current_user)


@routes.route("/video-feed")
def video_feed():
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")
