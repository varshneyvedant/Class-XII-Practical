# CBSE Project Audit Report

This document outlines the audit and simplification plan for adapting the project to meet the requirements of a CBSE Class XII Computer Science project for the 2025-26 academic session.

## 1. File & Module Audit

Here is a list of all project files and the plan for their adaptation.

| File/Module | Complexity Summary | Decision | Justification & CBSE Topic Mapping |
| :--- | :--- | :--- | :--- |
| `app.py` | Core Flask application with complex routing, business logic, and multiple user roles. | **SIMPLIFY** | The core logic is valuable but must be simplified. We will remove user roles, complex queries, and advanced features. It maps to: **Python Functions**, **Python-SQL Connectivity**, and **Basic Web Concepts**. |
| `requirements.txt` | Contains production-level and complex dependencies. | **SIMPLIFY** | Dependencies like `gunicorn` (production server) and `pdfkit` (complex PDF generation) are out of scope. We will reduce this to just `Flask`. Maps to: **Python Libraries**. |
| `seed.sql` | Contains initial data for the database. | **KEEP** | This is a good way to provide sample data. The SQL is simple and fits the syllabus. Maps to: **SQL / Database Management**. |
| `build.sh` | A shell script, likely for automated builds or deployment. | **REMOVE** | Automated deployment scripts are outside the scope of a school project. The application will be run directly via `python app.py`. |
| `static/css/style.css` | Standard CSS for styling the web pages. | **KEEP** | Basic styling is fine and does not add significant complexity. It is not a core CS topic but is necessary for the presentation of the project. |
| `static/js/main.js` | Contains frontend JavaScript, potentially for complex features. | **SIMPLIFY** | Any complex JS (e.g., for graphs, analytics) will be removed. Basic JS for interactivity is acceptable if kept minimal. |
| `static/js/confetti.js` | Cosmetic JavaScript library for celebrations. | **REMOVE** | This is non-essential and adds unnecessary clutter. |
| `templates/` (directory) | Contains numerous HTML files for the Flask web application. | **SIMPLIFY** | We will remove templates related to the 'super_admin' role and other complex features (`super_admin_dashboard.html`, `manage_users.html`, etc.). The remaining templates will be kept. Maps to: **Basic HTML (as part of project presentation)**. |
| `leaderboard_pdf.html` | A template specifically for generating a PDF. | **REMOVE** | This is tied to the `pdfkit` library which is being removed. It will be replaced by a CSV export feature. |

## 2. Features Outside Scope & Proposed Replacements

The following features were identified as being outside the CBSE Class XII syllabus and have been slated for removal or simplification.

| Feature | Reason for Removal/Simplification | Proposed Replacement |
| :--- | :--- | :--- |
| **Gunicorn Web Server** | Production-grade server; too complex for a student project. | Use Flask's built-in development server, which is started via `app.run()`. |
| **PDF Generation (`pdfkit`)** | Requires external dependencies (`wkhtmltopdf`) and is complex to set up. | Implement a **CSV Export** feature using Python's standard `csv` library. This directly demonstrates **File Handling**. |
| **Dual Admin Roles (`admin`, `super_admin`)**| Role-based access control is an advanced topic and complicates the code significantly. | Simplify to a single **'admin'** role with all necessary permissions. |
| **JavaScript Graph (`/api/graph_data`)** | Involves API endpoints and a JS charting library, which is too advanced. | Remove the graph entirely. The leaderboard table is sufficient for displaying data. |
| **Predictive Analytics & What-If Scenarios** | These are presented as complex ML/AI features. | Remove the features from the web interface. The underlying logic could be kept as a simple, commented Python function to demonstrate algorithms, if desired. |
| **Environment Variables (`.env`)** | Adds an unnecessary layer of configuration management for a simple project. | Hardcode configuration variables (like the database name) directly into `app.py` with comments. |
| **Complex SQL Queries (CTEs)** | The `WITH` clause in the `get_school_standings` query is advanced SQL. | Rewrite the query using simpler `JOIN`s or break it into multiple, more understandable queries. |

## 3. Assumptions

- The primary goal is **pedagogical clarity**, not production-readiness. Simplifications will prioritize code that is easy to read and explain over code that is robust or scalable.
- The target user is a Class XII student who needs to understand and explain every part of the project. The final code should not contain any "magic" or unexplainable components.
- `sqlite3` is the preferred database system as it requires no separate installation and is part of the Python standard library, aligning perfectly with the syllabus.
- The core concept of a "leaderboard application" is suitable and will be retained. The simplification will focus on the implementation, not the idea.
