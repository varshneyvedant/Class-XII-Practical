# Project Report: Interschool Competition Leaderboard

| | |
| :--- | :--- |
| **Project Title:** | Interschool Competition Leaderboard |
| **Student Name:** | [Your Name Here] |
| **Class/Section:** | XII / [Your Section] |
| **Subject:** | Computer Science (083) |
| **Session:** | 2025-26 |

---

## 1. Project Objective

The objective of this project is to design and develop a web-based application to manage and display the live results of an inter-school competition. The application provides a public-facing leaderboard for viewers and a secure admin panel for organizers to manage the data.

The project is built using Python, the Flask web framework, and an SQLite database, with a focus on demonstrating the core concepts learned in the CBSE Class XII Computer Science syllabus.

## 2. Problem Solved

In many school competitions, results are often tallied manually on spreadsheets and announced only at the end of the day. This process can be slow, prone to errors, and lacks real-time engagement for participants and the audience.

This project solves this problem by providing a centralized, web-based platform that:
*   Calculates and displays school rankings automatically and in real-time.
*   Provides a simple and secure interface for administrators to enter results as they come in.
*   Ensures data persistence and integrity by using a database.
*   Allows for easy data export (as a CSV file) for record-keeping.

## 3. Key Technologies and Concepts Demonstrated

*   **Backend:** Python 3 with the Flask web framework.
*   **Database:** SQLite 3, managed via Python's built-in `sqlite3` library.
*   **Frontend:** Basic HTML and CSS.
*   **Core Concepts:**
    *   Client-Server Architecture.
    *   Database Management (DDL, DML with SQL).
    *   Python-SQL Connectivity.
    *   File Handling (CSV generation).
    *   Web Development Fundamentals (Routing, Sessions).
    *   Password Security (Hashing).

## 4. Key Code Snippets

Here are some representative code snippets from the project that highlight key syllabus topics.

### Snippet 1: Connecting to the Database (`app.py`)

This function establishes the connection to the SQLite database file. It is the first step for any database interaction.

```python
import sqlite3

DB_PATH = 'podium.db'

# connects to the database
def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
```

### Snippet 2: Fetching Data with SQL (`app.py`)

This snippet shows how data for the main leaderboard is fetched from the database using a `SELECT` query with a `JOIN`.

```python
def get_school_standings(conn):
    # ... (code to fetch and process results)
    results_query = """
        SELECT
            r.first_place_school, r.second_place_school, r.third_place_school,
            e.first_place_points, e.second_place_points, e.third_place_points
        FROM Results r
        JOIN Events e ON r.event_id = e.id
    """
    all_results = conn.execute(results_query).fetchall()
    # ... (Python code to calculate points)
    return standings_list
```

### Snippet 3: Inserting Data with a Parameterized Query (`app.py`)

This snippet shows how a new school is added to the database. It uses a parameterized query (`?`) to prevent SQL injection, which is a critical security practice.

```python
@app.route('/add_school', methods=['POST'])
def add_school():
    # ... (admin check)
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
    # ...
    return redirect(url_for('admin_dashboard'))
```

### Snippet 4: File Handling - Generating a CSV File (`app.py`)

This function demonstrates writing data to a CSV file in memory and serving it for download.

```python
import io
import csv

@app.route('/export_leaderboard_csv')
def export_leaderboard_csv():
    # ... (admin check and data fetching)

    string_io = io.StringIO()
    writer = csv.writer(string_io)

    # Write the header row
    writer.writerow(['Rank', 'School', 'Total Points', ...])

    # Write the data rows
    for school in standings:
        writer.writerow([school['rank'], school['school'], ...])

    # ... (code to create and return response)
```

## 5. Testing and Verification

The project was tested manually by performing the following actions:
*   Running the application and setting up the database.
*   Accessing the main leaderboard to ensure it displays correctly.
*   Logging in as an admin with correct and incorrect credentials.
*   Adding, editing, and submitting results to see if the leaderboard updates.
*   Adding and deleting schools.
*   Exporting the leaderboard as a CSV and verifying the contents of the downloaded file.

The application functions as expected according to these tests.
