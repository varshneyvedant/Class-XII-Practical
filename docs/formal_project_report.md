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

### **❖ Hardware Specifications:**

| S.NO | Name of Component | Specifications |
| :--- | :--- | :--- |
| 1. | Processor | Pentium IV+ |
| 2. | Ram | 512MB |
| 3. | Hard Disk | 20GB |
| 4. | Monitor | 15’’ Color monitor |

### **❖ Software Specifications:**

| S.NO | Name of Component | Specifications |
| :--- | :--- | :--- |
| 1. | Operation System | Windows 10 or above, macOS, or Linux |
| 2. | IDE | Any Python-supported IDE (e.g., VS Code, PyCharm, IDLE) |
| 3. | Database | SQLite 3 (built-in with Python) |
| 4. | Browser | Chrome, Firefox, etc. |
| 5. | Front End | HTML, CSS |
| 6. | Back End | Python (with Flask Framework) |

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
| `delete_school()` | Flask route that processes the action to delete a school. |
| `export_leaderboard_csv()`| Flask route that generates and serves the leaderboard as a downloadable CSV file. |

---

# **Python Code**

*(The full source code for `app.py` is to be pasted here.)*

```python
# The full content of the final app.py file goes here.
# For brevity in this generation, it is omitted, but it should be
# included in the final document.
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash
import io
import csv
import os

# ... (rest of the app.py code) ...
```

---

# **Output Screens**

**(This section is to be filled with screenshots from the running application.)**

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

# **Bibliography**

1.  Arora, Sumita. *Computer Science with Python*. Dhanpat Rai & Co.
2.  NCERT. *Computer Science - Class XII*.
3.  The Pallets Projects. *Flask Documentation*. Retrieved from https://flask.palletsprojects.com/
4.  The Python Software Foundation. *Python 3 Documentation*. Retrieved from https://docs.python.org/3/
