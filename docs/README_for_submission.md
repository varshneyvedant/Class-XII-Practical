# Submission Package: Interschool Competition Leaderboard

This directory contains the complete set of documents and artifacts for the CBSE Class XII Computer Science project submission for the 2025-26 session.

## Contents

1.  **`project_report_content.md`**:
    *   This is the main project report in Markdown format.
    *   It contains all 15 required sections, from the Title Page to the Annexure.
    *   This file can be used to generate the final `.pdf` and `.docx` reports.

2.  **`presentation_outline.txt`**:
    *   This file contains a slide-by-slide outline for the project presentation.
    *   It includes key talking points and topics to cover for each slide.

3.  **`../` (Root Directory)**:
    *   The complete, simplified, and final source code for the project is located in the parent directory.
    *   This code can be zipped to create the `Annexure_Full_Source.zip` file.

## How to Generate Final Documents

### PDF/DOCX Report

The `project_report_content.md` file is written in Markdown, a simple text format. You can convert it to `.pdf` or `.docx` using several methods:

*   **Microsoft Word:** Copy the entire content of the `.md` file and paste it into a new Word document. You can then apply the required formatting (fonts, line spacing) and save it as a `.docx` and export it as a `.pdf`.
*   **Online Converters:** There are many free online tools that can convert Markdown files to PDF or DOCX.
*   **Pandoc:** If you have Pandoc installed (a universal document converter), you can use a command like:
    ```bash
    pandoc project_report_content.md -o Project_Report.docx
    pandoc project_report_content.md -o Project_Report.pdf
    ```

### Screenshots

The project report contains placeholders like `[Screenshot of ...]`. You will need to manually capture these screenshots from the live project website, annotate them as needed, and insert them into your final Word/PDF document.

### ZIP Files

*   **Source Code:** Navigate to the project's root directory and create a ZIP file of all the contents. Name it `Annexure_Full_Source.zip`.
*   **Screenshots:** Create a folder, place all your captured screenshots inside it, and then create a ZIP file of that folder. Name it `Screenshots_and_Images.zip`.
