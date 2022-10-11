from flask import Flask, flash, redirect, render_template, request, session, url_for



app = Flask(__name__)
app.secret_key = "zZdASfFReTRT8"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html")
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)