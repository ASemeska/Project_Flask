
from flask import Flask, flash, redirect, render_template, request, session, url_for
import requests
import json

app = Flask(__name__)
app.secret_key = "zZdASfFReTRT8"


@app.route("/", methods=['GET'])
def home():
    req = requests.get('http://www.boredapi.com/api/activity/')
    data = json.loads(req.text)
    print(data['key'])
    return render_template("index.html", data = data)

# @app.route("/login", methods = ["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         session["user"] = user
#         return redirect(url_for("user"))
#     else:
#         return render_template("login.html")

# @app.route("/user")
# def user():
#     if "user" in session:
#         user = session["user"]
#         return render_template("user.html")
#     else:
#         return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)