import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://bvehvpteviuree:adca7e23172feea8862b82cc738b905c0b89be6ac3cad55adc9f5ee773829b78@ec2-54-235-92-244.compute-1.amazonaws.com:5432/d43tu5vgnh1pcn')
db = scoped_session(sessionmaker(bind=engine))

def main():

    #list all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes.")

    #Prompt user to choose a flight.
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
                        {"id": flight_id}).fetchone()
    
    # make sure flight is valid.
    if flight is None:
        print("Error: no such flight.")
        return

    #list passengers
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id=:flight_id",
                            {"flight_id": flight_id}).fetchall()

    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")


if __name__ == '__main__':
    main()