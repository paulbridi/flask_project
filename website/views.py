from flask import Blueprint, render_template, request, redirect, url_for, flash, Response, jsonify

import openai
import sys



views = Blueprint('views', __name__)

# Route to home page, including POST and GET methods
@views.route('/', methods=["POST","GET"])
def home():
    print(request.method)
    if request.method == "POST" and 'text-input-string' in request.form:

        # return render_template("info.html")
        print(request.form)

        # Set form response to text_i_string for python usage
        text_i_string = request.form["text-input-string"]

        # Call openAI w paramters to create completion string
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=text_i_string,
            max_tokens=100,
            temperature=.9
            # stream=True <-- creates generator object
        )
        return render_template("home.html", i_string=text_i_string,  resp=resp)
    return render_template("home.html")


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
