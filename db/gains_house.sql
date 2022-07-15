DROP TABLE members;
DROP TABLE sessions;
DROP TABLE gyms;
DROP TABLE booked_sessions;

CREATE TABLE gyms (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    length INT,
    capacity INT,
    level VARCHAR(255),
    description TEXT
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    nationality VARCHAR(255),
    mob_number VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE booked_sessions (
    id SERIAL PRIMARY KEY,
    booked_member INT NOT NULL REFERENCES members(id),
    session_booked INT NOT NULL REFERENCES sessions(id)
);

