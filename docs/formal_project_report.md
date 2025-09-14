# **A Project Report**
# **On**
# **Interschool Competition Leaderboard**

## For AISSCE 2025-26 Examination
## As a part of the Computer Science Course (083)

<br>
<br>

### **Submitted by:**
### Vedant Varshney
### Class: XII H
### Roll Number: [Your Roll Number]

<br>

### **Submitted to:**
### Ms. Deepshika Sethi
### Department of Computer Science

<br>
<br>

**Amity International School, Mayur Vihar**

---
<div style="page-break-after: always;"></div>

# **Certificate**

This is to certify that the Project entitled, **Interschool Competition Leaderboard** is a bonafide work done by **Vedant Varshney** of class **12 H**, Session 2025-26 in partial fulfillment of CBSE’s AISSCE Examination 2025-26 and has been carried out under my supervision and guidance.

<br>
<br>
<br>

**……………………………**
<br>
**Signature of Teacher Guide**
<br>
**(Ms. Deepshikha Sethi)**

---
<div style="page-break-after: always;"></div>

# **Acknowledgement**

I would like to express my special thanks of gratitude to my teacher **Ms. Deepshikha Sethi**, as well as our principal, who gave me this golden opportunity to do this wonderful project on the topic "Interschool Competition Leaderboard". This project helped me greatly in my research and allowed me to learn many new things about practical software development.

The project would not have been completed without the constant support and kind help of my teacher. I would also like to thank my parents and friends who supported and encouraged me throughout the development of this project within the limited time frame.

**Vedant Varshney**
**Class XII H**

---
<div style="page-break-after: always;"></div>

# **Executive Summary**

The "Interschool Competition Leaderboard" is a purpose-built web application designed to address the inefficiencies of manual score-keeping in school-level competitive events. The primary problem this project solves is the delay and potential for human error inherent in traditional systems, replacing them with a dynamic, real-time, and reliable solution.

The core of the project is a Python-based web server built using the **Flask** framework, which provides a user-friendly interface for both participants and administrators. Key features include a public-facing live leaderboard, a secure admin dashboard for managing results and schools, and a data export function. The application's data persistence is handled by an **SQLite** database, demonstrating robust database management concepts.

This project was developed specifically to align with the **Class XII CBSE Computer Science curriculum**. It serves as a practical demonstration of fundamental concepts, including Python programming, functions, data structures, database connectivity via the `sqlite3` module, SQL queries, and file handling. The system's architecture and implementation have been intentionally kept clear and straightforward to ensure every aspect is understandable and explainable, making it an ideal academic project.

---
<div style="page-break-after: always;"></div>

# **Index**

| S.No | CONTENTS | PAGE NO. |
| :--- | :--- | :--- |
| 1 | Introduction | |
| 2 | System Architecture & Design | |
| 3 | System Requirements | |
| 4 | Modules Imported & Functions Used | |
| 5 | Detailed Implementation & Code Explanation | |
| 6 | Testing and Validation | |
| 7 | Output Screens | |
| 8 | Future Enhancements | |
| 9 | Conclusion | |
| 10 | Bibliography | |
| 11 | Appendix A: Full Source Code (`app.py`) | |
| 12 | Appendix B: User Manual / Deployment Guide | |

---
<div style="page-break-after: always;"></div>

# **1. Introduction**

### **1.1. Objectives**
The primary objective of this project is to design and develop a fully functional client-server application that automates the management of results for an inter-school competition. The project aims to:
*   Provide a centralized, web-based platform for real-time score tracking.
*   Eliminate the delays and errors associated with manual result tallying.
*   Create a secure and intuitive interface for administrators to manage competition data.
*   Serve as a practical, hands-on application of the key programming and database management concepts covered in the CBSE Class XII Computer Science syllabus.

### **1.2. Advantages**
*   **Reduces Workload:** Automates score calculation and ranking.
*   **Real-Time Updates:** Instantly reflects new results on the public leaderboard.
*   **Data Persistence:** Securely stores all data in a robust SQLite database.
*   **Accessibility:** As a web application, it can be easily accessed by multiple users on a network.
*   **Data Integrity:** Prevents accidental data loss, for example, by blocking the deletion of a school that has existing results.

### **1.3. Core Technologies Used**
*   **Python:** The high-level programming language used for all backend logic. Chosen for its readability and powerful standard library.
*   **Flask:** A lightweight "micro" web framework for Python. Chosen for its simplicity and flexibility, which are ideal for building a focused, understandable web application without unnecessary complexity.
*   **SQLite 3:** A self-contained, serverless SQL database engine. Chosen because it is included with Python and requires no separate installation, making the project highly portable and easy to run.
*   **HTML/CSS:** Standard markup and styling languages used to structure and design the frontend user interface.

---
<div style="page-break-after: always;"></div>

# **2. System Architecture & Design**

### **2.1. System Architecture (Flowchart)**
The application follows a standard **Client-Server Architecture**. The interaction between components can be visualized as follows:

**[Placeholder for a Flowchart/Diagram]**

*   **Description of Flowchart:**
    1.  **User's Web Browser (Client):** The user opens a web browser and navigates to the application's URL (e.g., `http://127.0.0.1:5001`). This sends an HTTP request to the server.
    2.  **Flask Web Server (Backend):** The Flask application receives the request. It identifies which function needs to handle this specific URL (e.g., the `/` route is handled by the `standings_view()` function).
    3.  **Database Interaction:** The Flask function connects to the `podium.db` (SQLite) database to fetch, insert, or update data as required.
    4.  **Response Generation:** The function then renders an HTML template, populating it with the data retrieved from the database.
    5.  **HTTP Response:** The server sends the final HTML document back to the client's browser, which then displays the web page to the user.

### **2.2. Database Schema (ER Diagram)**
The database is designed with four tables to logically store the application's data.

**[Placeholder for an ER Diagram]**

*   **Description of ER Diagram:**
    *   **Entities:** `Users`, `Schools`, `Events`, `Results`.
    *   **Relationships:**
        *   An `Event` can have one set of `Results`. This is a one-to-one relationship enforced by making `event_id` a unique key in the `Results` table.
        *   A `School` can appear in many `Results`.
    *   **Key Attributes:**
        *   `Users`: `id` (Primary Key), `username`, `password_hash`.
        *   `Schools`: `id` (Primary Key), `name`.
        *   `Events`: `id` (Primary Key), `name`.
        *   `Results`: `id` (Primary Key), `event_id` (Foreign Key to Events), `first_place_school`, `second_place_school`, `third_place_school`.

---
<div style="page-break-after: always;"></div>

# **3. System Requirements**

### **❖ Minimum Hardware Specifications:**

| S.NO | Component | Specification |
| :--- | :--- | :--- |
| 1. | Processor | Dual Core @ 1.6GHz or equivalent |
| 2. | RAM | 512 MB |
| 3. | Hard Disk | 100 MB of free space |

### **❖ Software Specifications:**

| S.NO | Component | Specification |
| :--- | :--- | :--- |
| 1. | Operating System | Windows 10+, macOS 10.13+, or any modern Linux distribution |
| 2. | Core Technology | Python 3.10 or newer |
| 3. | Key Library | Flask Framework |
| 4. | Database | SQLite 3 (which is included with Python and requires no separate installation) |
| 5. | Client Software | A modern web browser (e.g., Google Chrome, Mozilla Firefox, Microsoft Edge) |

---
<div style="page-break-after: always;"></div>

# **4. Modules Imported & Functions Used**

*(This section provides a summary. Detailed explanations are in the next section.)*

### **Modules Imported**
*   **sqlite3:** For all database interactions.
*   **Flask:** For creating the web server and handling routes.
*   **werkzeug.security:** For secure password hashing.
*   **csv, io:** For the CSV file export feature.
*   **os:** To check for the database file's existence.

### **Functions Used**
A table summarizing the key functions in `app.py` and their purpose.
*(Abridged for brevity - see full list in `teacher_explanation.md`)*

| Function Name | Function Use |
| :--- | :--- |
| `get_db_connection()` | Connects to the SQLite database. |
| `init_db_on_startup()`| Automatically creates and seeds the database on first run. |
| `get_school_standings()`| Calculates school rankings from results. |
| `standings_view()` | Route to display the public leaderboard. |
| `admin_dashboard()` | Route to display the main admin control panel. |
| `delete_school()` | Deletes a school after checking for existing results (Data Integrity). |
| `export_leaderboard_csv()`| Generates and serves the leaderboard as a downloadable CSV file. |

---
<div style="page-break-after: always;"></div>

# **5. Detailed Implementation & Code Explanation**

This section explains the logic of key parts of the project, highlighting how they demonstrate concepts from the CBSE syllabus.

### **5.1. Database Initialization on Startup**
To make the application portable and easy to run, it automatically creates and seeds the database if the `podium.db` file is not found.
*   **Concept:** Program flow control, File I/O (`os.path.exists`).
*   **Code:**
    ```python
    def init_db_on_startup():
        if not os.path.exists(DB_PATH):
            print(f"Database file '{DB_PATH}' not found. Creating...")
            setup_database()

    # This line is called once when the app starts
    init_db_on_startup()
    ```

### **5.2. Leaderboard Calculation Logic**
The leaderboard is calculated in Python to make the logic clear and explainable.
*   **Concepts:** Data Structures (Dictionary, List), Sorting (multi-level key).
*   **Explanation:** The `get_school_standings()` function first fetches all results from the database. It then iterates through them, using a dictionary to aggregate the total points for each school. A fixed-point system (100/75/50) is used. Finally, the dictionary is converted to a list and sorted using a tuple `(total_points, first_places, ...)` as the key to handle tie-breaking correctly.

### **5.3. Admin Security: Password Hashing**
Passwords are never stored directly. A secure hash is created and stored instead.
*   **Concept:** Information security, Hashing, Use of libraries.
*   **Code Snippet:**
    ```python
    from werkzeug.security import generate_password_hash, check_password_hash

    # Storing a new user's password
    hashed_password = generate_password_hash(password, method='scrypt')
    # ... INSERT into database ...

    # Checking a password on login
    if user and check_password_hash(user['password_hash'], password):
        # ... login successful ...
    ```

### **5.4. Data Integrity: Preventing Orphaned Records**
The application ensures that a school with existing results cannot be deleted.
*   **Concept:** Database Integrity, Relational Logic.
*   **Explanation:** Before deleting a school, the `delete_school()` function runs a `SELECT` query to check if the school's name appears in the `Results` table. If it does, the deletion is blocked and an error message is shown. This prevents a situation where a result refers to a school that no longer exists.

### **5.5. File Handling: CSV Export**
This feature demonstrates writing data to a file and serving it over the web.
*   **Concept:** File Handling (`io`, `csv` modules).
*   **Code Snippet:**
    ```python
    import io
    import csv

    @app.route('/export_leaderboard_csv')
    def export_leaderboard_csv():
        # ... get standings data ...
        string_io = io.StringIO() # Create an in-memory text file
        writer = csv.writer(string_io)
        writer.writerow(['Rank', 'School', 'Total Points', ...]) # Write header
        for school in standings:
            writer.writerow([...]) # Write data rows

        # ... code to create and return the file response ...
    ```
---
<div style="page-break-after: always;"></div>

# **6. Testing and Validation**

The application was tested manually to ensure all features work correctly and handle errors gracefully.

| Test Case ID | Test Description | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | Access the main leaderboard page (`/`). | The page loads and displays the table of schools from sample data. | The page loaded and displayed the table correctly. | Pass |
| TC-02 | Attempt to log in with incorrect credentials. | An error message "Wrong username or password" is displayed. | The error message was displayed correctly. | Pass |
| TC-03 | Log in with correct credentials (`admin`/`password`). | Redirected to the Admin Dashboard successfully. | The user was redirected successfully. | Pass |
| TC-04 | Submit a result for a pending event. | The event moves from "Pending" to "Submitted". | The functionality worked as expected. | Pass |
| TC-05 | Attempt to delete a school with existing results. | Deletion is blocked and an error message is displayed. | The error message was displayed correctly. | Pass |
| TC-06 | Delete a school that has no results. | The school is removed from the list. | The school was removed successfully. | Pass |
| TC-07 | Click the "Export as CSV" button. | A file `leaderboard.csv` is downloaded. | The file was downloaded and contained the correct data. | Pass |

---
<div style="page-break-after: always;"></div>

# **7. Output Screens**

**(This section is to be filled with high-resolution, annotated screenshots from the running application.)**

**[Screenshot 1: The Main Leaderboard Page]**
*Caption: The public-facing leaderboard, showing schools ranked by total points. The top 3 ranks are highlighted with special colors. (Annotate: Point to a highlighted row).*

**[Screenshot 2: The Admin Dashboard]**
*Caption: The main admin control panel, showing forms to submit results and manage schools. (Annotate: Circle the "Submit Result" form and the "Manage Schools" table).*

**[Screenshot 3: Database View Before Submitting a Result]**
*Caption: A view of the `Results` table in "DB Browser for SQLite" before a new result is added. Note the existing rows.*

**[Screenshot 4: Database View After Submitting a Result]**
*Caption: The `Results` table after submitting a new result. Note the newly added row, demonstrating a successful `INSERT` operation. (Annotate: Draw an arrow to the new row).*

---
<div style="page-break-after: always;"></div>

# **8. Future Enhancements**

This project provides a solid foundation that can be extended with more advanced features. The following are potential areas for future development:
*   **Multi-User Roles:** Implement a more complex user system with different roles (e.g., 'Judges', 'Event Coordinators') who have different permissions.
*   **Historical Data:** Add functionality to archive and view results from previous years or competitions.
*   **Data Visualization:** Integrate a charting library to create visual representations of the data, such as a bar chart of the top 5 schools.
*   **Real-time Updates:** Use technologies like WebSockets or AJAX to update the leaderboard live on the user's screen without requiring a page refresh.

---
<div style="page-break-after: always;"></div>

# **9. Conclusion**

This project successfully achieved its objective of creating a functional, database-driven web application for managing competition results. It serves as a comprehensive, practical demonstration of the key programming and data management skills outlined in the CBSE Class XII Computer Science syllabus.

The development process involved designing a logical database schema, writing backend code in Python with the Flask framework to manipulate and serve data, and creating a simple but effective user interface with HTML/CSS. Key concepts like data integrity, secure password handling, and file I/O were successfully implemented and documented. The final application is robust, easy to use, and provides a clear solution to the problem of manual score-keeping.

---
<div style="page-break-after: always;"></div>

# **10. Bibliography**

1.  Arora, Sumita. *Computer Science with Python*. Dhanpat Rai & Co.
2.  NCERT. *Computer Science - Class XII*.
3.  The Pallets Projects. *Flask Documentation*. Retrieved from https://flask.palletsprojects.com/
4.  The Python Software Foundation. *Python 3 Documentation*. Retrieved from https://docs.python.org/3/
5.  *SQLite Documentation*. Retrieved from https://www.sqlite.org/docs.html

---
<div style="page-break-after: always;"></div>

# **11. Appendix A: Full Source Code (`app.py`)**

```python
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import io
import csv
import os

app = Flask(__name__)
app.secret_key = 'silico_battles_2025_winner'

# database stuff
DB_PATH = 'podium.db'

# connects to the database
def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# -- DATABASE SETUP FUNCTIONS --
# These functions are used to set up the database for the first time.
# They are not part of the main web application, but are helper utilities.

def create_tables(conn):
    """
    Creates all the necessary tables for the application if they don't already exist.
    This is a good example of executing SQL DDL (Data Definition Language) commands from Python.
    """
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            -- The 'role' column is simplified to just 'admin'.
            -- In the original project, this was more complex ('super_admin', 'admin').
            role TEXT NOT NULL DEFAULT 'admin'
        );
        CREATE TABLE IF NOT EXISTS Events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            results_entered INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS Results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER UNIQUE NOT NULL REFERENCES Events(id),
            first_place_school TEXT,
            second_place_school TEXT,
            third_place_school TEXT,
            submitted_at DATETIME NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Schools (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
        -- The AuditLog table is removed for simplicity.
        -- It was used to track user actions, which is an advanced feature.
    ''')
    print("Tables created successfully.")

def seed_data(conn):
    """
    Populates the database with some initial sample data from an SQL file.
    This demonstrates reading from a file and executing SQL DML (Data Manipulation Language).
    """
    try:
        with open('db/seed.sql') as f:
            conn.executescript(f.read())
        print("Database seeded with initial data.")
    except FileNotFoundError:
        print("'db/seed.sql' not found. Skipping seeding.")
    except Exception as e:
        print(f"An error occurred during seeding: {e}")

def create_admin_user(conn, username, password):
    """
    Creates the first admin user.
    This function demonstrates:
    1. Hashing a password before storing it (a crucial security practice).
    2. Inserting data into a table using a parameterized query to prevent SQL injection.
    """
    try:
        # Hash the password for security. Never store plain text passwords!
        # The 'scrypt' method is a modern, secure hashing algorithm.
        hashed_password = generate_password_hash(password, method='scrypt')
        conn.execute(
            'INSERT INTO Users (username, password_hash, role) VALUES (?, ?, ?)',
            (username, hashed_password, 'admin')
        )
        conn.commit()
        print(f"Admin user '{username}' created successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists. Skipping creation.")
    except Exception as e:
        print(f"An error occurred creating admin user: {e}")

def setup_database():
    """
    A single function to set up the entire database.
    It connects to the DB, creates tables, seeds data, and creates a default admin.
    This is helpful for getting the project running quickly.
    """
    print("--- Setting up the database ---")
    conn = get_db_connection()
    try:
        with conn:
            create_tables(conn)
            seed_data(conn)
            # For demonstration, a default admin user is created.
            # In a real application, this should be handled more securely.
            create_admin_user(conn, 'admin', 'password')
    finally:
        conn.close()
        print("--- Database setup complete ---")

def get_school_standings(conn):
    """
    Calculates the leaderboard standings for all schools.
    This function demonstrates a practical use of SQL for data aggregation.
    The original query was complex (using a CTE), so it has been simplified
    to be more understandable for a student.
    """
    # Define the fixed points for each place. This simplifies the logic significantly.
    POINTS_FIRST = 100
    POINTS_SECOND = 75
    POINTS_THIRD = 50

    # Step 1: Get all results. We no longer need to join with the Events table for points.
    results_query = "SELECT first_place_school, second_place_school, third_place_school FROM Results"
    all_results = conn.execute(results_query).fetchall()

    # Step 2: Calculate points and placings for each school in Python.
    # This approach is easier to explain than a very complex SQL query.
    # It demonstrates the use of a dictionary (a key CBSE topic) to aggregate data.
    standings = {}
    for result in all_results:
        # Award points for 1st place
        if result['first_place_school']:
            school = result['first_place_school']
            standings.setdefault(school, {'total_points': 0, 'first': 0, 'second': 0, 'third': 0})
            standings[school]['total_points'] += POINTS_FIRST
            standings[school]['first'] += 1

        # Award points for 2nd place
        if result['second_place_school']:
            school = result['second_place_school']
            standings.setdefault(school, {'total_points': 0, 'first': 0, 'second': 0, 'third': 0})
            standings[school]['total_points'] += POINTS_SECOND
            standings[school]['second'] += 1

        # Award points for 3rd place
        if result['third_place_school']:
            school = result['third_place_school']
            standings.setdefault(school, {'total_points': 0, 'first': 0, 'second': 0, 'third': 0})
            standings[school]['total_points'] += POINTS_THIRD
            standings[school]['third'] += 1

    # Step 3: Convert the dictionary to a list of dictionaries for sorting.
    standings_list = []
    for school_name, data in standings.items():
        standings_list.append({
            'school': school_name,
            'total_points': data['total_points'],
            'first_places': data['first'],
            'second_places': data['second'],
            'third_places': data['third']
        })

    # Step 4: Sort the list to determine ranks.
    # Sorting is done by total points, then by number of 1st places, etc.
    # This is a good example of a multi-level sort.
    standings_list.sort(key=lambda x: (x['total_points'], x['first_places'], x['second_places'], x['third_places']), reverse=True)

    return standings_list

# -- PUBLIC ROUTES --
# These routes are accessible to anyone without logging in.

@app.route('/')
def standings_view():
    """
    Displays the main leaderboard page.
    This is the homepage of the application.
    """
    conn = get_db_connection()
    standings_raw = get_school_standings(conn)

    # Add ranks to the standings data. This logic handles ties correctly.
    standings_with_ranks = []
    rank = 0
    last_score = (-1, -1, -1, -1) # A tuple to track the last score for tie-breaking
    for i, school in enumerate(standings_raw):
        current_score = (school['total_points'], school['first_places'], school['second_places'], school['third_places'])
        if current_score != last_score:
            rank = i + 1
        standings_with_ranks.append(dict(school, rank=rank))
        last_score = current_score

    # Get the time of the last result submission.
    # The timezone logic has been removed for simplicity.
    last_updated_row = conn.execute("SELECT MAX(submitted_at) FROM Results").fetchone()
    last_updated_time = last_updated_row[0] if last_updated_row and last_updated_row[0] else None

    # Get all individual event results to display at the bottom of the page.
    all_results_query = """
        SELECT e.name, r.first_place_school, r.second_place_school, r.third_place_school
        FROM Results r JOIN Events e ON r.event_id = e.id ORDER BY e.name ASC
    """
    all_results = conn.execute(all_results_query).fetchall()
    conn.close()

    return render_template('standings.html', schools=standings_with_ranks, last_updated=last_updated_time, all_results=all_results)

@app.route('/school/<school_name>')
def school_details(school_name):
    """
    Displays a page with detailed results for a single school.
    This demonstrates fetching and displaying filtered data for a specific entity.
    """
    conn = get_db_connection()
    try:
        # Get the school's rank by processing the full leaderboard
        standings_raw = get_school_standings(conn)
        current_rank = "N/A"
        total_points = 0

        # This logic correctly calculates ranks, including handling for ties
        rank_counter = 0
        last_score = (-1, -1, -1, -1)
        for i, school in enumerate(standings_raw):
            current_score = (school['total_points'], school['first_places'], school['second_places'], school['third_places'])
            if current_score != last_score:
                rank_counter = i + 1

            if school['school'] == school_name:
                current_rank = rank_counter
                total_points = school['total_points']
                break

            last_score = current_score

        # Get all the positions the school has achieved.
        positions_query = """
            SELECT e.name AS event_name,
                   CASE
                       WHEN r.first_place_school = ? THEN '1st Place'
                       WHEN r.second_place_school = ? THEN '2nd Place'
                       WHEN r.third_place_school = ? THEN '3rd Place'
                   END AS position
            FROM Results r JOIN Events e ON r.event_id = e.id
            WHERE r.first_place_school = ? OR r.second_place_school = ? OR r.third_place_school = ?
            ORDER BY e.name;
        """
        positions = conn.execute(positions_query, (school_name, school_name, school_name, school_name, school_name, school_name)).fetchall()

        # Create a summary of 1st, 2nd, 3rd places
        summary = {'1st Place': 0, '2nd Place': 0, '3rd Place': 0}
        for pos in positions:
            if pos['position'] in summary:
                summary[pos['position']] += 1

        return render_template('school_details.html',
                               school_name=school_name,
                               results=positions,
                               summary=summary,
                               total_points=total_points,
                               rank=current_rank)
    finally:
        # This 'finally' block ensures the database connection is always closed,
        # even if an error occurs in the 'try' block. This is good practice.
        if conn:
            conn.close()

# -- ADMIN ROUTES --
# These routes are for administrators to manage the application data.

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles the admin login.
    Demonstrates form handling (POST request) and session management.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()
        conn.close()

        # check_password_hash is a security function to compare the entered password
        # with the stored hash. This is a very important security concept.
        if user and check_password_hash(user['password_hash'], password):
            # Store user info in the session to keep them logged in
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Wrong username or password.", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    """
    Logs the user out by clearing the session.
    """
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

def is_admin():
    """
    A helper function to check if a user is logged in.
    """
    return 'user_id' in session

@app.route('/admin_dashboard')
def admin_dashboard():
    """
    The main dashboard for admins.
    It shows forms to add/edit results and manage schools.
    """
    if not is_admin():
        flash("You must be logged in to see this page.", "danger")
        return redirect(url_for('login'))

    conn = get_db_connection()

    # Get all events to populate the dropdowns
    all_events = conn.execute('SELECT e.id, e.name, e.results_entered, r.first_place_school, r.second_place_school, r.third_place_school FROM Events e LEFT JOIN Results r ON e.id = r.event_id ORDER BY e.name').fetchall()

    # Get all schools for dropdowns
    schools = [row['name'] for row in conn.execute("SELECT name FROM Schools ORDER BY name ASC").fetchall()]

    # Get all schools for the management list
    all_schools_for_management = conn.execute('SELECT * FROM Schools ORDER BY name ASC').fetchall()

    conn.close()

    pending_events = [e for e in all_events if not e['results_entered']]
    submitted_events = [e for e in all_events if e['results_entered']]

    return render_template('admin_dashboard.html',
                           pending_events=pending_events,
                           submitted_events=submitted_events,
                           schools=schools,
                           all_schools_for_management=all_schools_for_management)

@app.route('/submit_result', methods=['POST'])
def submit_result():
    """
    Handles the form submission for adding a new event result.
    """
    if not is_admin():
        return redirect(url_for('login'))

    event_id = request.form['event_id']
    first = request.form['first_place']
    second = request.form['second_place']
    third = request.form['third_place']

    # Basic validation: ensure a school isn't in multiple places.
    # A list can be converted to a set to find unique items.
    if len(set(filter(None, [first, second, third]))) < len(list(filter(None, [first, second, third]))):
        flash("A school cannot be in multiple places for one event.", "danger")
        return redirect(url_for('admin_dashboard'))

    conn = get_db_connection()
    try:
        with conn:
            # Using a parameterized query to prevent SQL injection.
            conn.execute('''
                INSERT INTO Results (event_id, first_place_school, second_place_school, third_place_school, submitted_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (event_id, first, second, third, datetime.now()))
            conn.execute('UPDATE Events SET results_entered = 1 WHERE id = ?', (event_id,))
        flash('Results submitted successfully!', 'success')
    except sqlite3.IntegrityError:
        flash("Results for this event have already been submitted. Please edit them instead.", "danger")
    finally:
        conn.close()

    return redirect(url_for('admin_dashboard'))

@app.route('/edit_result/<int:event_id>', methods=['GET', 'POST'])
def edit_result(event_id):
    """
    Handles editing an existing result.
    Shows a form on GET and processes the update on POST.
    """
    if not is_admin():
        return redirect(url_for('login'))

    conn = get_db_connection()
    if request.method == 'POST':
        first = request.form['first_place']
        second = request.form['second_place']
        third = request.form['third_place']

        if len(set(filter(None, [first, second, third]))) < len(list(filter(None, [first, second, third]))):
            flash("A school cannot be in multiple places for one event.", "danger")
        else:
            with conn:
                conn.execute('''
                    UPDATE Results SET first_place_school = ?, second_place_school = ?, third_place_school = ?, submitted_at = ?
                    WHERE event_id = ?
                ''', (first, second, third, datetime.now(), event_id))
            flash('Results updated successfully!', 'success')

        conn.close()
        return redirect(url_for('admin_dashboard'))

    # For GET request, show the edit form with existing data
    result = conn.execute('SELECT * FROM Results WHERE event_id = ?', (event_id,)).fetchone()
    if not result:
        flash('No results found for this event.', 'warning')
        conn.close()
        return redirect(url_for('admin_dashboard'))

    event = conn.execute('SELECT * FROM Events WHERE id = ?', (event_id,)).fetchone()
    schools = [row['name'] for row in conn.execute("SELECT name FROM Schools ORDER BY name ASC").fetchall()]
    conn.close()

    return render_template('edit_result.html', result=result, event=event, schools=schools)

@app.route('/add_school', methods=['POST'])
def add_school():
    """
    Handles adding a new school.
    """
    if not is_admin():
        return redirect(url_for('login'))

    school_name = request.form['name'].strip()
    if school_name:
        conn = get_db_connection()
        try:
            with conn:
                conn.execute('INSERT INTO Schools (name) VALUES (?)', (school_name,))
            flash(f"School '{school_name}' added!", "success")
        except sqlite3.IntegrityError:
            flash(f"School '{school_name}' already exists.", "danger")
        finally:
            conn.close()
    else:
        flash("School name cannot be empty.", "danger")

    return redirect(url_for('admin_dashboard'))

@app.route('/delete_school/<int:school_id>', methods=['POST'])
def delete_school(school_id):
    """
    Handles deleting a school.
    Important: It checks if the school has results before deleting.
    This demonstrates the concept of foreign key constraints and data integrity.
    """
    if not is_admin():
        return redirect(url_for('login'))

    conn = get_db_connection()
    school_name = conn.execute('SELECT name FROM Schools WHERE id = ?', (school_id,)).fetchone()['name']

    # Check if school has participated in any events
    results_check = conn.execute('''
        SELECT 1 FROM Results WHERE ? IN (first_place_school, second_place_school, third_place_school)
    ''', (school_name,)).fetchone()

    if results_check:
        flash(f"Cannot delete '{school_name}' as it has existing results.", "danger")
    else:
        with conn:
            conn.execute('DELETE FROM Schools WHERE id = ?', (school_id,))
        flash(f"School '{school_name}' deleted.", "success")

    conn.close()
    return redirect(url_for('admin_dashboard'))

# -- FILE HANDLING DEMO --
# This route demonstrates exporting data to a CSV file, a key CBSE topic.
@app.route('/export_leaderboard_csv')
def export_leaderboard_csv():
    """
    Generates a CSV file of the current leaderboard standings.
    This function demonstrates:
    1. Fetching data from the database.
    2. Using the `io` and `csv` standard libraries.
    3. Creating a file in memory.
    4. Sending the file to the user as a download.
    """
    if not is_admin():
        return redirect(url_for('login'))

    conn = get_db_connection()
    standings = get_school_standings(conn)
    conn.close()

    # Use the `io` module to create an in-memory text file.
    # This avoids having to save the file to disk on the server.
    string_io = io.StringIO()

    # Use the `csv` module to write to the file.
    # This is the standard way to handle CSV data in Python.
    writer = csv.writer(string_io)

    # Write the header row
    writer.writerow(['Rank', 'School', 'Total Points', '1st Places', '2nd Places', '3rd Places'])

    # Write the data rows
    rank = 0
    last_score = (-1, -1, -1, -1)
    for i, school in enumerate(standings):
        current_score = (school['total_points'], school['first_places'], school['second_places'], school['third_places'])
        if current_score != last_score:
            rank = i + 1
        writer.writerow([
            rank,
            school['school'],
            school['total_points'],
            school['first_places'],
            school['second_places'],
            school['third_places']
        ])
        last_score = current_score

    # Prepare the response to send the file to the user.
    mem = io.BytesIO()
    mem.write(string_io.getvalue().encode('utf-8'))
    mem.seek(0)
    string_io.close()

    response = make_response(mem.getvalue())
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=leaderboard.csv'

    return response

def init_db_on_startup():
    """
    Initializes the database if it doesn't exist.
    This is suitable for deployment environments where interactive prompts are not possible.
    """
    if not os.path.exists(DB_PATH):
        print(f"Database file '{DB_PATH}' not found. Creating and seeding a new one.")
        setup_database()
    else:
        print(f"Database file '{DB_PATH}' already exists. Skipping initialization.")

# Initialize the database when the application starts
init_db_on_startup()

# -- MAIN EXECUTION --
if __name__ == '__main__':
    # This block runs when the script is executed directly (e.g., `python app.py`).
    # It's useful for local development and testing.
    # For deployment, a WSGI server like Gunicorn will import the 'app' object directly,
    # so this block will not be executed.

    # Start the Flask development web server.
    # `debug=True` is useful for development as it shows detailed errors
    # and automatically reloads the server when code changes.
    app.run(debug=True, port=5001)
```

---
<div style="page-break-after: always;"></div>

# **12. Appendix B: User Manual / Deployment Guide**

### **12.1. Installation**
1.  **Prerequisites:** Ensure you have Python 3.10 or a newer version installed on your system.
2.  **Download Source Code:** Download or clone the project repository to your local machine.
3.  **Install Dependencies:** Open a terminal or command prompt, navigate to the project's root folder, and run the following command to install the necessary Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### **12.2. First-Time Execution**
The first time you run the application, it will automatically create and set up the database for you.
1.  In your terminal, from the project's root folder, run the application:
    ```bash
    python app.py
    ```
2.  You will see messages in the terminal indicating that the database `podium.db` is being created and seeded with sample data. A default admin user (`username: admin`, `password: password`) will also be created.
3.  The Flask development server will start, typically on `http://127.0.0.1:5001`.

### **12.3. Using the Application**
1.  **View Leaderboard:** Open a web browser and go to `http://127.0.0.1:5001` to see the public leaderboard.
2.  **Admin Login:** Click the "Admin Login" button and use the default credentials to access the admin dashboard.
3.  **Manage Data:** From the dashboard, you can submit new results, edit existing ones, and manage the list of participating schools.
