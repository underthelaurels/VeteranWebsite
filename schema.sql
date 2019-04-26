-- Tables and Data surrounding a user

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS service_info;
DROP TABLE IF EXISTS employee_info;
DROP TABLE IF EXISTS employer_info;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS community_service_events;
DROP TABLE IF EXISTS jobs;

-- CREATE TABLE employee_info (
--     employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     status TEXT NOT NULL
-- );

-- CREATE TABLE employer_info (
--     employer_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company TEXT NOT NULL,
--     email TEXT,
--     phone_number TEXT
-- );

-- CREATE TABLE service_info (
--     service_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     branch TEXT NOT NULL,
--     years INTEGER
-- );

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    firstName TEXT,
    lastName TEXT, 
    email TEXT,
    isEmployer INTEGER
);

-- Tables for the Chat system

CREATE TABLE messages (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sent TEXT NOT NULL,
    message TEXT NOT NULL,
    channel_id INTEGER NOT NULL,
    sender TEXT NOT NULL,
    sender_color TEXT NOT NULL
);


-- Tables for the Community Service section

CREATE TABLE community_service_events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT NOT NULL, 
    time TEXT,
    street_address TEXT,
    city TEXT,
    state TEXT,
    zipcode INTEGER
);


-- Tables for the Employment section

CREATE TABLE jobs (
    job_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    industry TEXT,
    time_posted TEXT,
    due_date TEXT,
    street_address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zipcode INTEGER NOT NULL
);
