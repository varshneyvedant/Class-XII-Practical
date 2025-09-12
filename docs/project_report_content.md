# **Project Report**

---

## **Title Page**

**Project Title:** Interschool Competition Leaderboard

**A Project Report Submitted for the Partial Fulfillment of the
CBSE Class XII (Session 2025-26) Practical Examination**

**Submitted by:**
Vedant Varshney
Class XII H

**Submitted to:**
Ms. Deepshika Sethi
Department of Computer Science

**School:**
Amity International School, Mayur Vihar

---

## **Certificate**

This is to certify that **Vedant Varshney**, a student of **Class XII H**, has successfully completed the research on the project titled "**Interschool Competition Leaderboard**" under the guidance of **Ms. Deepshika Sethi** during the academic year 2025-26 in partial fulfillment of the Computer Science practical examination conducted by CBSE.

---
**(Signature of Principal)**

---
**(Signature of Teacher)**

---
**(Signature of External Examiner)**

---

## **Acknowledgement**

I would like to express my special thanks of gratitude to my teacher, **Ms. Deepshika Sethi**, as well as our principal, who gave me the golden opportunity to do this wonderful project on the topic "Interschool Competition Leaderboard", which also helped me in doing a lot of research and I came to know about so many new things.

Secondly, I would also like to thank my parents and friends who helped me a lot in finalizing this project within the limited time frame.

**Vedant Varshney**
**Class XII H**

---

## **Abstract**

The "Interschool Competition Leaderboard" is a web-based application designed to automate the process of managing and displaying results for school-level competitive events. The project replaces traditional manual or spreadsheet-based methods with a dynamic, real-time system built using Python, the Flask web framework, and an SQLite database.

The application features a public-facing leaderboard that displays school rankings based on a fixed scoring system. It also includes a secure, password-protected admin dashboard where authorized users can manage event results and participating schools. Key functionalities demonstrated include database management with Python, web-based file handling via CSV export, and fundamental web security practices like password hashing. The project's primary objective is to serve as a practical demonstration of the core concepts prescribed in the CBSE Class XII Computer Science syllabus.

---

## **1. Introduction**

### **1.1. Overview**
In any competitive environment, the timely and accurate dissemination of results is crucial. For inter-school fests and competitions, this process is often handled manually, leading to delays and a lack of real-time engagement. This project aims to solve this problem by creating a web-based platform that provides live, dynamic leaderboards.

### **1.2. How I Simplified This Project**
The initial version of this project contained many advanced, industry-standard features that are outside the scope of the Class XII syllabus. To make it a suitable and explainable academic project, I performed a significant simplification:
*   **Removed Advanced Features:** I removed complex features like dual admin roles, PDF generation, and JavaScript-based data charts.
*   **Simplified the Backend:** I rewrote complex SQL queries to be more straightforward and replaced third-party libraries with standard Python ones where possible (e.g., using `csv` for file handling).
*   **Focused on Core Concepts:** The final version of the project focuses squarely on demonstrating the core CBSE topics: Python functions, connecting to a SQL database with the `sqlite3` module, and file handling.

### **1.3. Objectives**
*   To design and develop a client-server application using Python Flask.
*   To implement a persistent data storage system using an SQLite database.
*   To demonstrate proficiency in SQL and Python-SQL connectivity.
*   To showcase practical file handling by exporting data to a CSV file.
*   To create a secure admin interface for data management.

---

## **2. Literature Review / Background**

The project is built upon well-established technologies and concepts in web development.
*   **Python:** A high-level, interpreted programming language known for its readability and extensive standard library. It serves as the backbone of the application's logic.
*   **Flask:** A lightweight "micro" web framework for Python. It provides the essential tools for handling web requests, managing user sessions, and rendering HTML pages without imposing a rigid structure, making it ideal for smaller projects and for learning.
*   **SQLite:** A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It is the most used database engine in the world. Being file-based and part of the Python standard library, it requires no separate server installation, making it perfect for this project.
*   **HTML/CSS:** The standard markup and styling languages used to create the structure and appearance of the web pages displayed in the user's browser.

---

## **3. Requirements**

### **3.1. Functional Requirements**
*   The system shall display a public leaderboard of all schools, ranked by score.
*   The system shall allow an administrator to log in to a secure dashboard.
*   The administrator shall be able to add/edit results for events.
*   The administrator shall be able to add/remove participating schools.
*   The administrator shall be able to export the leaderboard data as a CSV file.

### **3.2. Non-Functional Requirements**
*   **Security:** The admin dashboard must be password-protected. Passwords must be stored securely using hashing.
*   **Usability:** The user interface should be simple, intuitive, and easy to navigate.
*   **Simplicity:** The code should be well-commented and easy to understand for a Class XII student.
*   **Portability:** The application should run on any system with Python installed, with minimal setup.

---

## **4. System Design**

### **4.1. Architecture**
The application follows a standard **Client-Server Architecture**.

*   **Client:** The user's web browser (e.g., Chrome, Firefox), which requests pages and displays the HTML content it receives.
*   **Server:** The Python Flask application (`app.py`), which runs on a computer, listens for requests from clients, processes them, interacts with the database, and sends back a response.

**[Diagram: A simple client-server architecture diagram showing the Browser, Flask Server, and SQLite Database.]**

### **4.2. Database Design (ER Diagram)**
The database consists of four main tables: `Users`, `Events`, `Schools`, and `Results`.

*   **Users:** Stores the login credentials for the admin.
*   **Schools:** Stores the names of all participating schools.
*   **Events:** Stores the names of all competition events.
*   **Results:** This is the central table, linking an event to the winning schools. It has a one-to-one relationship with `Events`.

**[Diagram: A simple ER diagram showing the four tables and their relationships.]**

**Schema Details:**
*   `Users (id, username, password_hash, role)`
*   `Schools (id, name)`
*   `Events (id, name, results_entered)`
*   `Results (id, event_id, first_place_school, second_place_school, third_place_school, submitted_at)`

---

## **5. Implementation**

The project was implemented in Python using the Flask framework. Below are key code snippets that demonstrate core concepts.

### **5.1. Database Connection (`app.py`)**
This function establishes the connection to the `podium.db` file. `conn.row_factory = sqlite3.Row` is a helpful setting that allows accessing columns by name.
```python
def get_db_connection():
    conn = sqlite3.connect('podium.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn
```

### **5.2. Leaderboard Calculation (`app.py`)**
This function calculates the school standings. It fetches all results and uses a Python dictionary to aggregate the scores based on a fixed point system (100/75/50).
```python
def get_school_standings(conn):
    POINTS_FIRST = 100
    POINTS_SECOND = 75
    POINTS_THIRD = 50

    results_query = "SELECT first_place_school, second_place_school, third_place_school FROM Results"
    all_results = conn.execute(results_query).fetchall()

    standings = {}
    for result in all_results:
        # ... (logic to add points to schools in the standings dictionary) ...

    # ... (logic to convert dict to a sorted list) ...
    return standings_list
```

### **5.3. Admin Login and Session Management (`app.py`)**
This route handles the admin login. Upon successful authentication, it stores the `user_id` in the `session` object to keep the user logged in.
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # ... (code to get username/password from form) ...
        user = conn.execute('SELECT * FROM Users WHERE username = ?', (username,)).fetchone()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            return redirect(url_for('admin_dashboard'))
        # ... (else, show error) ...
    return render_template('login.html')
```

---

## **6. Testing**

The application was tested manually with a set of test cases to ensure all functionalities work as expected.

| Test Case ID | Test Description | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | Access the main leaderboard page. | The page loads and displays the table of schools from sample data. | The page loaded and displayed the table correctly. | Pass |
| TC-02 | Attempt to log in with incorrect admin credentials. | An error message "Wrong username or password" is displayed. | The error message was displayed correctly. | Pass |
| TC-03 | Log in with correct admin credentials (`admin`/`password`). | The user is redirected to the Admin Dashboard. | The user was redirected successfully. | Pass |
| TC-04 | Submit a result for a pending event. | The event moves from "Pending" to "Submitted" and the main leaderboard updates. | The functionality worked as expected. | Pass |
| TC-05 | Add a new school from the admin dashboard. | The new school appears in the list of schools. | The school was added successfully. | Pass |
| TC-06 | Delete a school that has no results. | The school is removed from the list. | The school was removed successfully. | Pass |
| TC-07 | Click the "Export as CSV" button. | A file named `leaderboard.csv` is downloaded with the correct data. | The file was downloaded and contained the correct data. | Pass |

---

## **7. User Manual / Installation Guide**

1.  **Prerequisites:** Python 3.10+ and `pip`.
2.  **Download:** Download or clone the project source code.
3.  **Install Dependencies:** Open a terminal in the project folder and run: `pip install -r requirements.txt`
4.  **Run the Application:** In the same terminal, run: `python app.py`
5.  **Database Setup:** The application will automatically create and seed the database (`podium.db`) on the first run.
6.  **Access:** Open a web browser and navigate to `http://127.0.0.1:5001`.

---

## **8. Screenshots**

**[Screenshot 1: The Main Leaderboard Page]**
*Caption: The public-facing leaderboard, showing schools ranked by total points. The top 3 ranks are highlighted.*

**[Screenshot 2: The School Details Page]**
*Caption: The detailed view for a single school, showing its rank, total points, and performance in each event.*

**[Screenshot 3: The Admin Login Page]**
*Caption: The secure login portal for the site administrator.*

**[Screenshot 4: The Admin Dashboard]**
*Caption: The main admin control panel, showing forms to submit results and manage schools.*

**[Screenshot 5: The Exported CSV File]**
*Caption: The `leaderboard.csv` file opened in a spreadsheet application, showing the exported data.*

---

## **9. Conclusion and Future Scope**

### **9.1. Conclusion**
This project successfully demonstrates the creation of a dynamic, database-driven web application using Python and Flask. It meets all the specified objectives and effectively applies the key concepts from the CBSE Class XII Computer Science curriculum in a practical and tangible way. The process of simplifying the project from a more complex initial state was also a valuable learning experience in focusing on core requirements.

### **9.2. Future Scope**
*   **User Roles:** Introduce more user roles, such as "Event Coordinator," who can only enter results for their specific event.
*   **Data Visualization:** Re-introduce data visualization features, such as charts showing score progression over time.
*   **Real-time Updates:** Implement WebSockets to allow the leaderboard to update automatically in real-time without needing a page refresh.
*   **Online Registration:** Add a feature to allow schools to register for the competition directly through the website.

---

## **10. Bibliography**

*   The Python Software Foundation. *Python Language Reference*. Available at: https://www.python.org
*   The Pallets Projects. *Flask Documentation*. Available at: https://flask.palletsprojects.com/
*   The SQLite Consortium. *About SQLite*. Available at: https://www.sqlite.org/
*   CBSE. *Senior School Curriculum (2025-26)*. Available at: https://cbseacademic.nic.in/

---

## **11. Annexure (Full Code Listing)**

The full source code for this project is contained within the repository. The primary files are:
*   `app.py` (Main application logic)
*   `db/schema.sql` (Database schema)
*   `db/seed.sql` (Sample data)
*   `python_sql_demo.py` (Connectivity demo)
*   `templates/` (Directory containing all HTML files)
*   `static/` (Directory containing CSS and JS files)
