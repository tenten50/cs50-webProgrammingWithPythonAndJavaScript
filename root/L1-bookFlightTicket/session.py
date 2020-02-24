from flask import Flask, render_template, url_for, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"]= []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("session.html", notes = session["notes"])


if __name__ == '__main__':
    app.run(host="192.168.3.3", port="5000", debug=True)

