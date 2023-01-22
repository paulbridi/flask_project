from flask import Blueprint, render_template, request, redirect, url_for, flash

views = Blueprint('views', __name__)

@views.route('/', methods=["POST","GET"])
def home():
    if request.method == "POST":
        i_string = request.form["input-string"]
        print(i_string)
        return render_template("home.html", i_string=i_string)
    else:
        return render_template("home.html")
