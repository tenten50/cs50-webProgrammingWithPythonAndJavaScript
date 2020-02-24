CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT into passengers 
    (name,flight_id)
    VALUES ('Alice', 1);

INSERT into flights 
    (origin,destination,duration)
    VALUES ('NEW YORK', 'London', 415);

SELECT * FROM flights;

SELECT origin, destination FROM flights;

SELECT * FROM flights WHERE id = 3;

SELECT COUNT(*) FROM flights WHERE origin in ('New York', 'NEW YORK');

SELECT COUNT(*) FROM flights WHERE origin LIKE '%N%';

UPDATE flights SET duration = 430 WHERE origin = 'New York' and destination = 'London';

DELETE FROM flights WHERE destination = 'London';

SELECT origin, COUNT(*) FROM flights GROUP BY origin;

SELECT destination, COUNT(*) FROM flights GROUP BY destination HAVING COUNT(*) > 1;

SELECT origin, destination, name from flights JOIN passengers ON flights.id = passengers.flight_id;