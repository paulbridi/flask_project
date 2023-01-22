from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/info/')
def info():
    return render_template("info.html")

@auth.route('/contact/')
def logout():
    return render_template("contact.html")

@auth.route('/sign-up/')
def sign_up():
    return render_template("sign-up.html")
