import pandas as pd
import os
from pathlib import Path

# Input and output folders
input_folder = 'Vornamen'  # Replace with your actual folder if necessary
output_folder = 'Vornamen_dublicate_removal'  # Folder to store cleaned files

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all CSV files in the input folder
for csv_file in Path(input_folder).glob('Vornamen_*.csv'):
    print(f"Processing: {csv_file.name}")

    # Read the CSV file using your settings
    df = pd.read_csv(csv_file, sep=';', encoding='latin1')

    # Show original column names (for debugging)
    print("Original columns:", df.columns.tolist())

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Drop unwanted columns if they exist
    df = df.drop(columns=[col for col in ['geschlecht', 'position'] if col in df.columns])

    # Group by 'vorname' and sum 'anzahl'
    df_summed = df.groupby('vorname', as_index=False)['anzahl'].sum()

    # Build output file path (keep same filename)
    output_path = Path(output_folder) / csv_file.name

    # Save the cleaned file
    df_summed.to_csv(output_path, index=False)
    print(f"Saved cleaned file to: {output_path}\n")
