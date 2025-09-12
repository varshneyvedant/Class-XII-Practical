# Teacher & Viva Voce Explanation Guide

This document is designed to help the student understand and explain the project during their viva voce examination.

## 1. Module-by-Module Explanation

Here is a simple breakdown of each important file and what to say about it.

### `app.py` - The Core Application

*   **What it is:** This is the main file of our project. It's a Python script that runs a web server using the **Flask** library.
*   **CBSE Topics:** It demonstrates **Python Functions** (each `@app.route` is a function that handles a web request), **Python-SQL Connectivity** (it connects to the `podium.db` database to get data), and **Session Management** (for the admin login).
*   **How to explain:** "This file contains the main logic for our web application. We use the Flask library to create different web pages (routes). For example, the `standings_view` function gets data from the database and displays the main leaderboard. The `login` function handles the admin login and uses sessions to remember the user."

### `python_sql_demo.py` - Database Connectivity Demo

*   **What it is:** This is a separate, simple Python script created specifically to demonstrate the database concepts required by the CBSE syllabus.
*   **CBSE Topics:** It directly shows **Python-SQL Connectivity**, including `connect()`, `cursor()`, `execute()`, `fetchall()`, `commit()`, and using parameterized queries to prevent SQL injection.
*   **How to explain:** "This script is a simple demo to show how Python connects to our SQLite database. It shows the 7 main steps: importing `sqlite3`, connecting to the database, creating a cursor, executing a query, fetching the data, committing changes, and closing the connection. We used this to test our database logic."

### `db/schema.sql` and `db/seed.sql` - Database Structure

*   **What they are:** `schema.sql` contains the `CREATE TABLE` commands that define the structure of our database (the tables and columns). `seed.sql` contains `INSERT` commands to fill the database with some sample data so the app isn't empty.
*   **CBSE Topics:** This demonstrates **SQL (DDL and DML)**. `CREATE TABLE` is Data Definition Language (DDL), and `INSERT` is Data Manipulation Language (DML).
*   **How to explain:** "`schema.sql` is the blueprint for our database. It defines the `Users`, `Events`, `Results`, and `Schools` tables. `seed.sql` provides the initial data for these tables, like the list of events and schools."

### `/export_leaderboard_csv` route (in `app.py`) - File Handling

*   **What it is:** This is a special function in `app.py` that generates a CSV file of the leaderboard when a user clicks the "Export as CSV" button.
*   **CBSE Topics:** It demonstrates **File Handling** in Python, specifically working with CSV files using the standard `csv` module and sending a file to the user over the web using the `io` module.
*   **How to explain:** "To show file handling, we created a feature to export the leaderboard. This function gets the data, uses the `csv` library to write it into the correct format, and then sends it to the browser as a downloadable file named `leaderboard.csv`."

### `templates/` directory - The Frontend

*   **What it is:** This directory contains all the HTML files that make up the user interface of our website. Flask uses these templates to generate the web pages.
*   **CBSE Topics:** While not a core CS topic, it shows the practical application of programming by creating a user-friendly interface. It uses basic HTML and Jinja2 templating.
*   **How to explain:** "The `templates` folder holds the HTML structure of our website. We use a base template called `layout.html` for the common parts like the header and footer, and other files like `standings.html` for specific pages. This is how we separate our Python logic from the presentation."

## 2. Likely Viva Questions & Model Answers

**Q1: What is the purpose of your project?**
*   **Answer:** "Our project is a web application that manages and displays a live leaderboard for an inter-school competition. It allows a public audience to see the current standings and an administrator to log in and update the results for various events."

**Q2: What technologies did you use?**
*   **Answer:** "We used Python for the backend logic, the Flask library to create the web server, SQLite for the database, and basic HTML/CSS for the frontend. All the database interaction is done using Python's standard `sqlite3` library."

**Q3: How does your project use a database? Can you show me the code?**
*   **Answer:** "We use an SQLite database named `podium.db` to store all our data. In `app.py`, we have a function called `get_db_connection()` that connects to the database. We then use a cursor to execute SQL queries, like `SELECT` to fetch the leaderboard data and `INSERT` to add new results. You can also see a clear demonstration in `python_sql_demo.py`."

**Q4: How did you ensure the security of the admin login?**
*   **Answer:** "We did not store the admin's password in plain text. Instead, we used the `werkzeug.security` library to create a **hash** of the password before storing it in the database. When the admin tries to log in, we hash their entered password and compare it to the stored hash. This is a secure method because even if someone accesses the database, they cannot see the original password."

**Q5: Your project involves file handling. Where is this demonstrated?**
*   **Answer:** "We demonstrated file handling with our 'Export as CSV' feature. In `app.py`, there is a function called `export_leaderboard_csv`. It fetches the current leaderboard data, uses the standard `csv` library to write the data into a CSV format in memory, and then sends it to the user's browser as a downloadable file named `leaderboard.csv`."

**Q6: What is the purpose of the `requirements.txt` file?**
*   **Answer:** "The `requirements.txt` file lists all the external Python libraries that our project depends on. In our simplified project, it only contains `Flask`. This file allows another person to easily install the correct dependencies using the command `pip install -r requirements.txt`."

**Q7: What is a "session" in a web application? How did you use it?**
*   **Answer:** "A session is a way for a web server to store information about a user across multiple requests. We used it for our admin login. When the admin successfully logs in, we store their `user_id` in the session. For any page that requires admin access, we first check if the `user_id` is present in the session. When they log out, we clear the session."

**Q8: Can you explain the SQL query you used to calculate the leaderboard?**
*   **Answer:** "To calculate the leaderboard, we first fetch all the results from the `Results` table and join it with the `Events` table to get the points for each place. Then, in Python, we use a dictionary to loop through these results and aggregate the total points and the number of 1st, 2nd, and 3rd place finishes for each school. Finally, we sort this data using a multi-level sort, first by total points, then by 1st places, and so on, to get the final ranks."

## 3. In-Class Demo Script

Here is a simple script you can follow to demonstrate the project to your teacher.

1.  **Start the application:**
    *   Open a terminal, navigate to the project folder.
    *   Run `python app.py`. If it's the first time, type `y` to set up the database.
    *   Say: "I am now starting the web server."

2.  **Show the main page:**
    *   Open a web browser to `http://127.0.0.1:5001`.
    *   Say: "This is the main leaderboard page. It is visible to everyone and shows the current school rankings based on the sample data we loaded."

3.  **Demonstrate the Admin Login:**
    *   Click on "Admin Login".
    *   Enter a wrong password first to show the error message. Say: "The system prevents login with incorrect credentials."
    *   Now log in with **username:** `admin` and **password:** `password`.
    *   Say: "After a successful login, I am redirected to the admin dashboard."

4.  **Demonstrate Adding a Result:**
    *   On the admin dashboard, find an event in the "Pending Events" list.
    *   Select schools for 1st, 2nd, and 3rd place from the dropdowns and click "Submit Result".
    *   Say: "Here, the admin can submit new results. This data is inserted into our database."
    *   Go back to the main leaderboard page (by clicking the "Podium 🏆" title) and show that the standings have been updated.

5.  **Demonstrate CSV Export:**
    *   From the admin dashboard, click the "Export as CSV" button.
    *   A file named `leaderboard.csv` will be downloaded.
    *   Open the file in a spreadsheet program to show the data.
    *   Say: "This demonstrates our file handling feature, where the current leaderboard is exported to a CSV file."

6.  **Log out:**
    *   Click "Logout".
    *   Say: "The logout button clears the session, and I am returned to the login page."
