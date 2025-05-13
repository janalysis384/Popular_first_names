import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Ask for the name to plot
name_to_plot = input("Enter a first name (case-insensitive): ").strip().capitalize()

# Step 1: Load all CSV files
all_files = glob.glob("Vornamen_dublicate_removal/Vornamen_*.csv")

df_list = []

# Step 2: Read each file and add 'Year'
for file in all_files:
    year = int(os.path.basename(file).split('_')[1].split('.')[0])  # Extract year from filename
    temp_df = pd.read_csv(file, sep=',', encoding='latin1')  # Adjusted for comma separator
    temp_df.columns = temp_df.columns.str.replace('\ufeff', '').str.strip().str.capitalize()  # Normalize column names
    temp_df['Year'] = year
    df_list.append(temp_df)

# Step 3: Combine all into one DataFrame
df = pd.concat(df_list, ignore_index=True)

# Step 4: Filter for the selected name
filtered_df = df[df['Vorname'].str.lower() == name_to_plot.lower()]

# Step 5: Check if name exists in data
if filtered_df.empty:
    print(f"No data found for the name '{name_to_plot}'.")
else:
    # Step 6: Group and plot
    grouped = filtered_df.groupby('Year')['Anzahl'].sum()

    plt.figure(figsize=(10, 6))
    grouped.plot(marker='o')
    plt.title(f'Häufigkeit des Namens "{name_to_plot}" über die Jahre')
    plt.xlabel('Jahr')
    plt.ylabel('Anzahl')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Step 7: Save the plot
safe_filename = f"{name_to_plot.lower()}_trend.png"
plt.figure(figsize=(10, 6))
grouped.plot(marker='o')
plt.title(f'Häufigkeit des Namens \"{name_to_plot}\" über die Jahre')
plt.xlabel('Jahr')
plt.ylabel('Anzahl')
plt.grid(True)
plt.tight_layout()
plt.savefig(safe_filename)
print(f"✅ Plot saved as: {safe_filename}")