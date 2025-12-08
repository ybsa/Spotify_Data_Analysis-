# Spotify Data Analysis Pipeline

## Project Structure

- **`Data/`**: Contains the SQLite database (`spotify.db`) and extracted CSV datasets.
- **`Report/`**: Contains the final generated analysis report (`Spotify_Findings_Report.pdf`).
- **`Raw_Data/`**: Contains the original raw CSV source files.
- **`etl_pipeline.py`**: Python script for ETL (Extract, Transform, Load) operations.
- **`Spotify_Analysis.ipynb`**: Jupyter Notebook for Data Analysis, Visualization, and PDF generation.

## How to Run

### 1. Requirements

Execute the Python script to process the raw data and update the database:

```bash
python etl_pipeline.py
```

*This will create `spotify.db` and extracted CSVs in the `Data/` folder.*

### 3. Run Analysis & Generate Report

Open `Spotify_Analysis.ipynb` in Jupyter Notebook or Jupyter Lab and execute all cells.

- This will merge the datasets, clean the data, generate visualizations, and save the final report to **`Report/Spotify_Findings_Report.pdf`**.*
