import pandas as pd
from sqlalchemy import create_engine
import os

# Configuration
DB_FILE = 'Data/spotify.db'

# Define datasets (Source path, Table name, Output Path)
DATASETS = [
    {
        "source": "Raw_Data/track_data_final.csv",
        "table": "tracks_final",
        "output": "Data/extracted_final.csv"
    },
    {
        "source": "Raw_Data/spotify_data clean.csv",
        "table": "tracks_cleaned",
        "output": "Data/extracted_cleaned.csv"
    }
]

def upload_data(csv_path, db_name, table_name):
    """Reads CSV and uploads to SQLite database."""
    if not os.path.exists(csv_path):
        print(f"Error: File not found at {csv_path}")
        return

    print(f"Reading data from {csv_path}...")
    try:
        df = pd.read_csv(csv_path)
        print(f"Data loaded. Shape: {df.shape}")
        
        engine = create_engine(f'sqlite:///{db_name}')
        print(f"Uploading to table '{table_name}'...")
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print("Upload successful!")
        
    except Exception as e:
        print(f"An error occurred during upload: {e}")

def extract_data(db_name, table_name, output_path):
    """Queries data from SQLite and saves to CSV."""
    print(f"Extracting data from table '{table_name}'...")
    try:
        engine = create_engine(f'sqlite:///{db_name}')
        query = f"SELECT * FROM {table_name}"
        df_extracted = pd.read_sql(query, engine)
        print(f"Data extracted. Shape: {df_extracted.shape}")
        df_extracted.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")
        
    except Exception as e:
        print(f"An error occurred during extraction: {e}")

if __name__ == "__main__":
    print("--- Starting Multi-File ETL Pipeline ---")
    
    for ds in DATASETS:
        print(f"\nProcessing {ds['source']}...")
        # 1. Upload
        upload_data(ds['source'], DB_FILE, ds['table'])
        # 2. Extract
        extract_data(DB_FILE, ds['table'], ds['output'])
    
    print("\n--- Pipeline Finished ---")
