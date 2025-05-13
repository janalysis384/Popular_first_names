import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('Vornamen_2010.csv', sep=';')  # Replace with your actual file name

# Clean column names
df.columns = df.columns.str.strip().str.capitalize()

# Get the top 5 names by 'Anzahl'
top5 = df.nlargest(5, 'Anzahl')

# Plot
plt.figure(figsize=(8, 5))
plt.bar(top5['Vorname'], top5['Anzahl'], color='skyblue')
plt.title('Top 5 Vornamen')
plt.xlabel('Vorname')
plt.ylabel('Anzahl')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
