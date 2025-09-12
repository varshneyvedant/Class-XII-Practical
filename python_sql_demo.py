# CBSE Class XII Computer Science Project
# Python-SQL Connectivity Demo
#
# This script demonstrates the fundamental steps required to connect a Python
# application to an SQLite database. It covers all the essential commands
# as prescribed in the CBSE syllabus.

import sqlite3
import os

# Define the path to the database file.
# Using os.path.join is a good practice for cross-platform compatibility.
DB_PATH = 'podium.db'

def demonstrate_python_sql_connectivity():
    """
    A function that encapsulates all the database operations for demonstration.
    """
    print("--- Python-SQL Connectivity Demo ---")

    # It's good practice to check if the database file exists.
    # For this demo, we assume the main application has already created it.
    if not os.path.exists(DB_PATH):
        print(f"Database file '{DB_PATH}' not found.")
        print("Please run the main application (`python app.py`) first to create the database.")
        return

    # Step 1: Connect to the database
    # The `sqlite3.connect()` function opens a connection to the SQLite database file.
    # If the file does not exist, it will be created.
    # The 'conn' object represents the database connection.
    try:
        conn = sqlite3.connect(DB_PATH)
        print(f"\n[SUCCESS] Connected to the database '{DB_PATH}'.")
    except sqlite3.Error as e:
        print(f"[ERROR] Could not connect to the database: {e}")
        return

    try:
        # Step 2: Create a cursor object
        # A cursor is used to execute SQL commands. You can think of it as a
        # pointer or a controller for the records in the database.
        cursor = conn.cursor()
        print("Cursor created successfully.")

        # --- DEMO 1: Reading data with SELECT ---
        print("\n--- 1. Reading Data (SELECT) ---")

        # Step 3: Execute an SQL query
        # The `cursor.execute()` method is used to run a single SQL command.
        sql_query = "SELECT name FROM Schools ORDER BY name LIMIT 5;"
        print(f"Executing query: \"{sql_query}\"")
        cursor.execute(sql_query)

        # Step 4: Fetch the results
        # `cursor.fetchall()` retrieves all the rows from the result of the query.
        # It returns a list of tuples.
        # Other fetch methods include `fetchone()` (for one row) and `fetchmany(size)`.
        schools = cursor.fetchall()

        print("\nTop 5 Schools:")
        if schools:
            for i, school in enumerate(schools):
                # Each 'school' is a tuple, e.g., ('School A',)
                print(f"  {i+1}. {school[0]}")
        else:
            print("No schools found in the database.")

        # --- DEMO 2: Inserting data with INSERT ---
        print("\n--- 2. Inserting Data (INSERT) ---")

        new_school_name = "CBSE Demo School"
        print(f"Attempting to insert a new school: '{new_school_name}'")

        # Step 5: Execute a parameterized query
        # To prevent SQL Injection attacks, always use '?' as placeholders for values.
        # Then, pass the values as a tuple to the `execute` method.
        # NEVER use f-strings or string formatting to build queries with user input.
        insert_query = "INSERT INTO Schools (name) VALUES (?);"

        try:
            cursor.execute(insert_query, (new_school_name,))

            # Step 6: Commit the transaction
            # When you modify the database (INSERT, UPDATE, DELETE), you must call
            # `conn.commit()` to save the changes permanently.
            conn.commit()
            print(f"[SUCCESS] Committed the new school to the database.")

            # Verify the insertion
            cursor.execute("SELECT name FROM Schools WHERE name = ?;", (new_school_name,))
            result = cursor.fetchone()
            if result:
                print(f"Verification successful: Found '{result[0]}' in the database.")
            else:
                print("[ERROR] Verification failed.")

        except sqlite3.IntegrityError:
            print(f"Could not add school '{new_school_name}' because it already exists.")
            # If the insert fails, we should roll back any partial changes.
            conn.rollback()
        except sqlite3.Error as e:
            print(f"[ERROR] An error occurred during insertion: {e}")
            conn.rollback()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Step 7: Close the connection
        # It's very important to close the connection when you're done with it
        # to free up resources.
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == '__main__':
    demonstrate_python_sql_connectivity()
