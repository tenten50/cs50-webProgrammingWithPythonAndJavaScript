import os
from flask import Flask, render_template, url_for, request, session
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://bvehvpteviuree:adca7e23172feea8862b82cc738b905c0b89be6ac3cad55adc9f5ee773829b78@ec2-54-235-92-244.compute-1.amazonaws.com:5432/d43tu5vgnh1pcn')
db = scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)

@app.route("/")
def index():
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book/", methods=["POST"])
def book():
    """book a flight"""

    #get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    if db.execute("SELECT * FROM flights WHERE id = :id",{"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id.")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",{"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html", message="You booked a ticket succeddfully!")





if __name__ == '__main__':
    app.run(host="192.168.3.3", port="5000", debug=True)