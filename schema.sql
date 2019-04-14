DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS service_info;
DROP TABLE IF EXISTS employee_info;
DROP TABLE IF EXISTS employer_info;

CREATE TABLE employee_info (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL
);

CREATE TABLE employer_info (
    employer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT NOT NULL,
    email TEXT,
    phone_number TEXT
);

CREATE TABLE service_info (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch TEXT NOT NULL,
    years INTEGER
);

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    firstName TEXT,
    lastName TEXT, 
    email TEXT,
    service_id INTEGER,
    employer_id INTEGER,
    employee_id INTEGER,
        FOREIGN KEY (service_id) REFERENCES service_info(service_id)
        FOREIGN KEY (employer_id) REFERENCES employer_info(employer_id)
        FOREIGN KEY (employee_id) REFERENCES employee_info(employee_id)
);

