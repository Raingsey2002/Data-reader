
This is a Streamlit-based dashboard application for reading and visualizing FMIS master data.

## Prerequisites

- [Python](https://www.python.org/downloads/) (Version 3.8 or higher recommended)
- [Git](https://git-scm.com/downloads)

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/Raingsey2002/Data-reader.git
    ```

2.  **Create and activate a virtual environment**:

    *   **Windows**:
        ```terminal
        python -m venv .venv
        .\.venv\Scripts\Activate
        ```
    *   **macOS/Linux**:
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the dashboard, run the following command from the project root (`Data-reader` folder):

```bash
streamlit run streamit_data_reader.py
```

The application will launch in your default web browser (usually at `http://localhost:8501`).

## Project Structure

- `streamit_data_reader.py`: Main entry point for the application.
- `pages/`: Contains individual page modules (e.g., `Report_page.py`, `Fmis_Entity.py`).
- `Excel files/`: Contains data files (.parquet, .xlsx) used by the application.
- `requirements.txt`: List of Python dependencies.

