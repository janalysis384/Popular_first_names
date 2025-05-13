import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# Step 1: Load all CSV files
all_files = glob.glob("Vornamen_dublicate_removal/Vornamen_*.csv")  # <- Update this path

df_list = []

# Step 2: Read each file and add 'Year'
for file in all_files:
    year = int(os.path.basename(file).split('_')[1].split('.')[0])  # Extract year from filename
    temp_df = pd.read_csv(file, sep=',', encoding= 'latin1'
                                                   '')  # Read with semicolon separator
    temp_df.columns = temp_df.columns.str.strip().str.capitalize()  # Clean column names
    temp_df['Year'] = year
    df_list.append(temp_df)

# Step 3: Combine all into one DataFrame
df = pd.concat(df_list, ignore_index=True)

# Step 4: Get top 5 names overall
top10_names = df.groupby('Vorname')['Anzahl'].sum().nlargest(5).index

# Step 5: Filter for those names
filtered_df = df[df['Vorname'].isin(top10_names)]

# Step 6: Pivot table for plotting
pivot_df = filtered_df.pivot_table(index='Year', columns='Vorname', values='Anzahl', aggfunc='sum')

# Step 7: Plot
pivot_df.plot(figsize=(12, 6), marker='o')
plt.title('Top 5 Vornamen')
plt.xlabel('Jahr')
plt.ylabel('Anzahl')
plt.grid(True)
plt.legend(title='Vorname')
plt.tight_layout()
plt.show()

# Step 8: Save
pivot_df.plot(figsize=(12, 6), marker='o')
plt.title('Top 5 Vornamen')
plt.xlabel('Jahr')
plt.ylabel('Anzahl')
plt.grid(True)
plt.legend(title='Vorname')
plt.tight_layout()
plt.savefig(f"top5_vornamen.png")
plt.close()