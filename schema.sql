-- Table 1: Laboratories
CREATE TABLE laboratories (
    lab_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lab_name TEXT NOT NULL UNIQUE,
    location TEXT NOT NULL
);

-- Table 2: Energy Logs
CREATE TABLE energy_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lab_id INTEGER NOT NULL,
    reading_kwh REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (lab_id) REFERENCES laboratories (lab_id) ON DELETE CASCADE
);

-- Data Insertion
INSERT INTO laboratories (lab_name, location) VALUES 
('Computer Lab 1', 'Intramuros Campus - 2nd Floor'),
('Computer Lab 2', 'Intramuros Campus - 3rd Floor');

INSERT INTO energy_logs (lab_id, reading_kwh) VALUES 
(1, 15.5),
(1, 18.2),
(2, 42.0),
(2, 38.5);