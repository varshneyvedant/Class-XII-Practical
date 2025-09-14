# **A Project Report**
# **On**
# **Interschool Competition Leaderboard**

## For AISSCE 2025-26 Examination
## As a part of the Computer Science Course (083)

### **Submitted by:**
### Vedant Varshney
### Class: XII H
### Roll Number: [Your Roll Number]

---

# **CERTIFICATE**

This is to certify that the Project entitled, **Interschool Competition Leaderboard** is a bonafide work done by **Vedant Varshney** of class **12 H**, Session 2025-26 in partial fulfillment of CBSE’s AISSCE Examination 2025-26 and has been carried out under my supervision and guidance.

<br>
<br>
<br>

**……………………………**
<br>
**Signature of teacher guide**
<br>
**(Ms. Deepshikha Sethi)**

---

# **Index**

| S.No | CONTENTS | PAGE NO. |
| :--- | :--- | :--- |
| 1 | Acknowledgement | 4 |
| 2 | Introduction | 5 |
| 3 | System Requirements | 7 |
| 4 | Modules Imported & Functions Used | 8 |
| 5 | Python Code | 11 |
| 6 | Output Screens | 12 |
| 7 | Bibliography | 13 |

---

# **Acknowledgement**

I would like to express my special thanks of gratitude to my teacher **Ms. Deepshikha Sethi**, who gave me this golden opportunity to do this wonderful project on the topic "Interschool Competition Leaderboard". This helped me in doing a lot of research and I came to know about so many new things. The project would not have been completed without her support and kind help.

I would also like to thank my parents and friends who supported me throughout the development of this project.

**Jaikrit Sethi**

---

# **Introduction**

### **Objectives of the Project**
*   This software is designed to manage and display live results for an inter-school competition in a smooth and effective manner.
*   The software is supported to eliminate and in some cases, reduce the hardships faced by existing manual systems, such as delays and human error.
*   This project aims to demonstrate the practical application of programming and database concepts learned in the Class XII curriculum.

### **Advantages of the Project**
1.  **Reduces Workload:** Automates the calculation of scores and rankings, reducing the manual workload on event organizers.
2.  **Real-Time Updates:** Provides live, up-to-the-minute standings for all participants and viewers.
3.  **Time Efficient:** Organizers can input results as they are announced, and the leaderboard reflects the changes instantly.
4.  **Data Persistence:** Securely stores all school, event, and result data in a database for future reference.
5.  **Accessibility:** Being a web application, it can be accessed by anyone with a web browser on the local network.

### **Limitations of the Project**
1.  **Single Admin User:** The project currently supports only one administrator account. It does not have a multi-user login system.
2.  **No Historical Data Tracking:** The system does not store historical leaderboards; it only shows the current state of the competition.

---

# **System Requirements**

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

# **Modules Imported & Functions Used**

### **Modules Imported**
1.  **sqlite3:** The standard Python library for connecting to and interacting with an SQLite database.
2.  **Flask:** The web framework used to build the application's routes and handle web requests.
3.  **werkzeug.security:** Used specifically for its `generate_password_hash` and `check_password_hash` functions to ensure password security.
4.  **csv & io:** Standard Python libraries used for the "Export to CSV" file handling feature.
5.  **os:** Used to check for the existence of the database file on startup.

### **Functions Used in Code**

| Function Name | Function Use |
| :--- | :--- |
| `get_db_connection()` | Connects to the SQLite database file and returns a connection object. |
| `create_tables()` | Executes SQL to create all the necessary tables if they don't exist. |
| `seed_data()` | Populates the database with initial sample data from `db/seed.sql`. |
| `create_admin_user()` | Creates the default admin user with a hashed password. |
| `setup_database()` | A helper function that calls the table creation, seeding, and user creation functions. |
| `init_db_on_startup()` | Checks if the database exists on startup and calls `setup_database()` if it doesn't. |
| `get_school_standings()`| The core logic to calculate school rankings based on results and fixed points. |
| `standings_view()` | Flask route to display the main public leaderboard page. |
| `school_details()` | Flask route to display the detailed results for a single school. |
| `login()` | Flask route to handle the admin login form and session creation. |
| `logout()` | Flask route to clear the user session and log the admin out. |
| `is_admin()` | A helper function to check if a user is currently logged in. |
| `admin_dashboard()` | Flask route to display the main dashboard for the logged-in admin. |
| `submit_result()` | Flask route that processes the form for submitting a new event result. |
| `edit_result()` | Flask route to display and process the form for editing an existing result. |
| `add_school()` | Flask route that processes the form for adding a new school. |
| `delete_school()` | Processes the school deletion. Includes a data integrity check to prevent deleting a school that has existing results. |
| `export_leaderboard_csv()`| Flask route that generates and serves the leaderboard as a downloadable CSV file. |

---

# **Python Code**

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
            # We can break here since we found our school
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

    conn.close()

    return render_template('school_details.html',
                           school_name=school_name,
                           results=positions,
                           summary=summary,
                           total_points=total_points,
                           rank=current_rank)

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

# **Output Screens**

**(This section is to be filled with screenshots from the running application.)**

### **Application UI Screenshots**

**[Screenshot 1: The Main Leaderboard Page]**
*Caption: The public-facing leaderboard, showing schools ranked by total points. The top 3 ranks are highlighted with special colors.*

**[Screenshot 2: The School Details Page]**
*Caption: The detailed view for a single school, showing its current rank, total points, and performance in each event.*

**[Screenshot 3: The Admin Login Page]**
*Caption: The secure login portal for the site administrator.*

**[Screenshot 4: The Admin Dashboard]**
*Caption: The main admin control panel, showing forms to submit results for pending events and to add or delete schools.*

**[Screenshot 5: The Exported CSV File]**
*Caption: The `leaderboard.csv` file opened in a spreadsheet application, showing the exported data.*

### **Database Interaction Screenshots**

**[Screenshot 6: Database View Before Submitting a Result]**
*Caption: A view of the `Results` table in "DB Browser for SQLite" before a new result is added. Note the existing rows.*

**[Screenshot 7: Database View After Submitting a Result]**
*Caption: The `Results` table after submitting a new result through the web application. Note the newly added row at the bottom, demonstrating a successful `INSERT` operation.*

**[Screenshot 8: Database View Before Editing a Result]**
*Caption: The `Results` table showing a specific row before an edit is made.*

**[Screenshot 9: Database View After Editing a Result]**
*Caption: The same row in the `Results` table after being modified via the "Edit" function in the application, demonstrating a successful `UPDATE` operation.*

---

# **Bibliography**

1.  Arora, Sumita. *Computer Science with Python*. Dhanpat Rai & Co.
2.  NCERT. *Computer Science - Class XII*.
3.  The Pallets Projects. *Flask Documentation*. Retrieved from https://flask.palletsprojects.com/
4.  The Python Software Foundation. *Python 3 Documentation*. Retrieved from https://docs.python.org/3/
