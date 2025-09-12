# CBSE Syllabus Mapping

This document maps the features and files of the "Interschool Competition Leaderboard" project to the specific units and topics of the CBSE Class XII Computer Science (083) syllabus for the 2025-26 session.

---

## Unit I: Computational Thinking and Programming – 2

This unit covers Python programming concepts. Our project demonstrates these in a practical, integrated manner.

| Syllabus Topic | Project Feature / File | Description |
| :--- | :--- | :--- |
| **Functions** | `app.py` | The entire web application is built using functions. Each route (e.g., `@app.route('/')`) is a Python function that takes a request and returns a response. Helper functions like `get_db_connection()` and `get_school_standings()` are also used to structure the code logically. |
| **File Handling (Text, Binary, CSV)** | `app.py` (CSV Export) | The project demonstrates **CSV file handling**. The `/export_leaderboard_csv` route uses the `csv` module to write leaderboard data to a file. It also uses the `io` module to handle the file in-memory, which is a good practice for web applications. |
| **Using Python Libraries** | `requirements.txt`, `app.py` | The project uses the external **Flask** library, installed via `pip` from `requirements.txt`. This demonstrates how to use third-party libraries to extend Python's functionality. |
| **Data Structures: Stack** | *(Conceptually Covered)* | While not an explicit stack implementation, the process of handling web requests in Flask follows a **call stack** model. Furthermore, the navigation history in a browser as a user clicks through the app is a real-world example of a stack, which can be mentioned in the viva. |
| **Data Structures: List & Dictionary** | `app.py` (`get_school_standings`) | The project extensively uses lists and dictionaries. For example, the `get_school_standings` function fetches data as a list of rows, processes it into a dictionary to aggregate points, and then converts it back to a sorted list of dictionaries to send to the template. |

---

## Unit II: Computer Networks

This unit covers the concepts of computer networks. The project itself is a web application, which is a direct, practical example of network concepts in action.

| Syllabus Topic | Project Feature / File | Description |
| :--- | :--- | :--- |
| **Web Server** | `app.py` (Flask Server) | The project runs on a **web server** (Flask's development server). This demonstrates the client-server model where the user's browser (client) sends requests to our Python application (server). |
| **Web Browser, URL, HTTP** | Entire Application | Students run the project by navigating to a **URL** (`http://127.0.0.1:5001`) in a **web browser**. The communication between the browser and the Flask server happens over the **HTTP** protocol. |
| **IP Address** | `127.0.0.1` | The address `127.0.0.1` is the **localhost IP address**, which is used to access the server running on the same machine. This is a practical example of an IP address. |
| **Client-Server Architecture**| Entire Application | The project is a perfect example of a **client-server application**. The Python code (`app.py`) acts as the server, handling logic and data, while the user's web browser acts as the client, sending requests and displaying the received HTML. |

---

## Unit III: Database Management

This unit covers database concepts, SQL, and interfacing Python with a SQL database.

| Syllabus Topic | Project Feature / File | Description |
| :--- | :--- | :--- |
| **Database Concepts** | `db/schema.sql` | The project demonstrates key database concepts: **relations/tables** (`Users`, `Events`), **attributes/columns**, and **tuples/rows**. The schema is designed to be relational. |
| **SQL: DDL (CREATE)** | `db/schema.sql` | The `CREATE TABLE` commands in this file are a direct example of **Data Definition Language (DDL)** used to define the database structure. |
| **SQL: DML (INSERT, SELECT, UPDATE, DELETE)** | `app.py`, `db/seed.sql` | The project uses all major DML commands: **INSERT** (in `seed.sql` and when adding results/schools), **SELECT** (to fetch data for all pages), **UPDATE** (when editing results), and **DELETE** (when removing a school). |
| **Python-SQL Connectivity** | `python_sql_demo.py`, `app.py` | This is a core feature. The project demonstrates the full workflow: `connect()` to the database, create a `cursor()`, `execute()` queries (including parameterized queries to prevent SQL injection), `fetchall()`/`fetchone()` to retrieve data, `commit()` changes, and `close()` the connection. The `python_sql_demo.py` file is a dedicated, commented example of this process. |
