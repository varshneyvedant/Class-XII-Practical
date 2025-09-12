-- This SQL script creates the database schema for the Podium application.
-- It is designed to be simple and easy to understand for a Class 12 student.
-- It demonstrates the use of CREATE TABLE, PRIMARY KEY, FOREIGN KEY (implicitly), and various data types.

-- The Users table stores login information for the admin.
-- The 'role' has been simplified to just 'admin' for this project.
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'admin'
);

-- The Events table stores the list of competitions.
CREATE TABLE IF NOT EXISTS Events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    results_entered INTEGER DEFAULT 0,
    first_place_points INTEGER DEFAULT 100,
    second_place_points INTEGER DEFAULT 75,
    third_place_points INTEGER DEFAULT 50
);

-- The Results table stores the winners for each event.
-- The event_id is a foreign key that links to the Events table.
CREATE TABLE IF NOT EXISTS Results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER UNIQUE NOT NULL REFERENCES Events(id),
    first_place_school TEXT,
    second_place_school TEXT,
    third_place_school TEXT,
    submitted_at DATETIME NOT NULL
);

-- The Schools table stores the list of participating schools.
CREATE TABLE IF NOT EXISTS Schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
