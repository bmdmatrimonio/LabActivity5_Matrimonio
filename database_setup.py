import sqlite3


def main():
    #Connect to SQLite database
    conn = sqlite3.connect("energy_monitor.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    #Schema Creation
    cursor.executescript("""
        DROP TABLE IF EXISTS energy_logs;
        DROP TABLE IF EXISTS laboratories;

        CREATE TABLE laboratories (
            lab_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lab_name TEXT NOT NULL UNIQUE,
            location TEXT NOT NULL
        );

        CREATE TABLE energy_logs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            lab_id INTEGER NOT NULL,
            reading_kwh REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (lab_id) REFERENCES laboratories (lab_id) ON DELETE CASCADE
        );
    """)
    print("Database schema created successfully.\n")

    #Data Insertion
    cursor.executescript("""
        INSERT INTO laboratories (lab_name, location) VALUES 
            ('Computer Lab 1', 'Intramuros Campus - 2nd Floor'),
            ('Computer Lab 2', 'Intramuros Campus - 3rd Floor');

        INSERT INTO energy_logs (lab_id, reading_kwh) VALUES 
            (1, 15.5),
            (1, 18.2),
            (2, 42.0),
            (2, 38.5);
    """)
    conn.commit()

    #Test Cases / Sample Queries

    print("=== Test Case 1: Retrieve All Laboratories ===")
    cursor.execute("SELECT * FROM laboratories;")
    for row in cursor.fetchall():
        print(f"Lab ID: {row[0]} | Name: {row[1]} | Location: {row[2]}")

    print("\n=== Test Case 2: Inner Join (Logs with Lab Names) ===")
    cursor.execute("""
        SELECT e.log_id, l.lab_name, e.reading_kwh, e.timestamp 
        FROM energy_logs e
        JOIN laboratories l ON e.lab_id = l.lab_id;
    """)
    for row in cursor.fetchall():
        print(f"Log ID: {row[0]} | {row[1]} | Consumption: {row[2]} kWh | Time: {row[3]}")

    print("\n=== Test Case 3: Aggregate Energy Reading Per Lab ===")
    cursor.execute("""
        SELECT l.lab_name, SUM(e.reading_kwh) as total_kwh, AVG(e.reading_kwh) as avg_kwh
        FROM laboratories l
        JOIN energy_logs e ON l.lab_id = e.lab_id
        GROUP BY l.lab_id;
    """)
    for row in cursor.fetchall():
        print(f"Lab: {row[0]} | Total: {row[1]:.2f} kWh | Avg: {row[2]:.2f} kWh")

    conn.close()


if __name__ == "__main__":
    main()