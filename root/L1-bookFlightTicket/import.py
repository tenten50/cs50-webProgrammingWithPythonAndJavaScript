import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://bvehvpteviuree:adca7e23172feea8862b82cc738b905c0b89be6ac3cad55adc9f5ee773829b78@ec2-54-235-92-244.compute-1.amazonaws.com:5432/d43tu5vgnh1pcn')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("./src/flights.csv")
    reader = csv.reader(f)
    for o, des, dur in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin": o, "destination": des, "duration": dur})
        print(f"Added flight from {o} to {des}, lasting {dur} minutes.")
    db.commit()

if __name__ == '__main__':
    main()