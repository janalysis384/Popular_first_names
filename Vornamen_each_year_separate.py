import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Get all Vornamen_*.csv files
all_files = glob.glob("Vornamen_dublicate_removal/Vornamen_*.csv")  # <-- change this to your folder path

# Loop through each file
for file in sorted(all_files):
    # Extract year from filename like Vornamen_2010.csv
    year = os.path.basename(file).split('_')[1].split('.')[0]

    # Load the CSV
    df = pd.read_csv(file, sep=',', encoding='latin1')  # adjust encoding if needed
    df.columns = df.columns.str.strip().str.capitalize()

    # Get top 5 names
    top5 = df.nlargest(5, 'Anzahl')

    # Plot
    plt.figure(figsize=(8, 5))
    plt.bar(top5['Vorname'], top5['Anzahl'], color='skyblue')
    plt.title(f'Top 5 Vornamen im Jahr {year}')
    plt.xlabel('Vorname')
    plt.ylabel('Anzahl')
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(f"top5_vornamen_{year}.png")
    plt.close()