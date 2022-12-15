from flask import Blueprint, render_template, Response
from flask_login import login_required, current_user

from Website.website.controllers.acess_level import requires_access_level
from Website.website.controllers.CStudent import CStudent


from Recognition.recognition import FaceRecognition


routes = Blueprint("routes", __name__)


@routes.route("/")
@login_required
def home():
    return render_template("index.html", user=current_user)

@routes.route("/video_feed")
@login_required
@requires_access_level(current_user, 1)
def video_feed():
    fr = FaceRecognition()
    return Response(fr.run_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')
            
@routes.route("/attendance")
@login_required
@requires_access_level(current_user, 1)
def attendance():
    return render_template("attendance.html", user=current_user, students=CStudent.get_students_attendance_done())

@routes.route("/students")
@login_required
@requires_access_level(current_user, 1)
def students():
    return render_template("students.html", user=current_user, students=CStudent.get_all_students())
