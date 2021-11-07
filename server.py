from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    # if "survey" not in session:
        # session["survey"] = []

    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__== "__main__":
    app.run(debug=True)