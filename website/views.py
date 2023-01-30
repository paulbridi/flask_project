from flask import Blueprint, render_template, request, Response, jsonify
from website.python_scripts.text_io import text_io


import os

views = Blueprint('views', __name__)

# Route to home page, including POST and GET methods
@views.route('/', methods=["POST","GET"])
def home():
    return render_template("home.html")

@views.route('/text_output/', methods=["POST"])
def text_output():
    text_i_string = request.form["input_text"]
    output_text = text_io(text_i_string)
    return output_text

@views.route('/info/')
def info():
    return render_template("info.html")

@views.route('/contact/')
def logout():
    return render_template("contact.html")

@views.route('/sign-up/')
def sign_up():
    return render_template("sign-up.html")

@views.route("/update_map", methods=["POST"])
def update_map():
    print("update_map route was called")

    # update the data for the specific component
    updated_map_data = [51.5384557, -0.0962833]
    return jsonify(updated_map_data)
