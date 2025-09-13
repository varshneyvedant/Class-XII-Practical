# Project: Interschool Competition Leaderboard

This project is a web application for tracking the live leaderboard and results of an inter-school competition. It has been adapted and simplified to be suitable for a CBSE Class XII Computer Science project for the 2025-26 session.

The core technologies used are Python, the Flask web framework, and an SQLite database. The focus is on demonstrating key concepts from the CBSE syllabus in a practical, easy-to-understand manner.

## Key Features (CBSE Adaptation)

*   **Live Leaderboard:** A public-facing page that shows the current school rankings, updated in real-time as results are entered.
*   **Admin Dashboard:** A password-protected area where an administrator can log in to:
    *   Submit results for different events.
    *   Edit previously submitted results.
    *   Add or remove participating schools.
*   **Python-SQL Connectivity:** All data is stored in an SQLite database (`podium.db`). The project demonstrates creating tables, inserting data, and fetching data using Python's `sqlite3` module.
*   **File Handling:** The project includes a feature to export the live leaderboard to a CSV file, demonstrating how to generate and serve files from a web application using Python's `csv` module.

## How to Run the Project

This project is designed to be simple to run with a standard Python installation.

### Prerequisites

*   Python 3.10 or newer.
*   `pip` (Python's package installer).

### Setup and Execution

1.  **Clone the repository or download the source code.**

2.  **Navigate to the project directory:**
    ```bash
    cd path/to/your/project
    ```

3.  **Install the required Python library (Flask):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database (First Time Only):**
    When you run the application for the first time, it will prompt you to set up the database. This will create the `podium.db` file, set up the necessary tables, and add some sample data.

    Run the application:
    ```bash
    python app.py
    ```

    In the terminal, you will be asked:
    `Do you want to set up the database? ... [y/n]:`

    Type `y` and press Enter. The database will be initialized, and a default admin user will be created with the credentials:
    - **Username:** `admin`
    - **Password:** `password`

5.  **Access the Application:**
    Once the server is running, open your web browser and go to:
    [http://127.0.0.1:5001](http://127.0.0.1:5001)

    You can view the leaderboard. To manage data, click on "Admin Login" and use the credentials above.

## Project Scope

This project was designed and developed from the ground up as a practical implementation of the concepts taught in the CBSE Class XII Computer Science curriculum. The focus is on clarity, readability, and directly mapping features to syllabus topics like Python-SQL connectivity, file handling, and web basics.
