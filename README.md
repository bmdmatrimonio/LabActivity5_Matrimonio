## Lab Activity 5: Data Modeling and Introduction to SQL

## Schema Description
This relational model consists of two entities:
1. **laboratories:** Stores information regarding specific computer laboratory rooms (lab_id, lab_name, location).
2. **energy_logs:** Tracks numerical energy consumption readings (log_id, lab_id, reading_kwh, timestamp). Linked to laboratories via a Foreign Key (lab_id).

## How to Run

1. Open your terminal or WSL Ubuntu environment.
2. Navigate to the project directory:
    `cd lab_activity_5`
3. Run the Python database script:
    `python3 database_setup.py`

## Sample Output:
Database schema created successfully.

=== Test Case 1: Retrieve All Laboratories ===
Lab ID: 1 | Name: Computer Lab 1 | Location: Intramuros Campus - 2nd Floor
Lab ID: 2 | Name: Computer Lab 2 | Location: Intramuros Campus - 3rd Floor

=== Test Case 2: Inner Join (Logs with Lab Names) ===
Log ID: 1 | Computer Lab 1 | Consumption: 15.5 kWh | Time: 2026-08-31 22:27:10
Log ID: 2 | Computer Lab 1 | Consumption: 18.2 kWh | Time: 2026-08-31 22:27:10
Log ID: 3 | Computer Lab 2 | Consumption: 42.0 kWh | Time: 2026-08-31 22:27:10
Log ID: 4 | Computer Lab 2 | Consumption: 38.5 kWh | Time: 2026-08-31 22:27:10

=== Test Case 3: Aggregate Energy Reading Per Lab ===
Lab: Computer Lab 1 | Total: 33.70 kWh | Avg: 16.85 kWh
Lab: Computer Lab 2 | Total: 80.50 kWh | Avg: 40.25 kWh
