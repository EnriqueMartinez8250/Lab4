import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to your CSV file
csv_file_path = 'Data.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)


df['Time_seconds'] = df['Time'] / 1000  # Adjust this line if your time unit is different


total_discharge_time = df['Time_seconds'].max()  # Total time of discharge
df['SoC'] = 1 - (df['Time_seconds'] / total_discharge_time)  # SoC decreases linearly

# Calculate 1-SoC for plotting
df['1-SoC'] = 1 - df['SoC']


window_size = 50  
df['Voltage_smooth'] = df['Voltage'].rolling(window=window_size, center=True).mean()

# Plotting Voltage vs. 1-SoC
plt.figure(figsize=(12, 6))
plt.plot(df['1-SoC'], df['Voltage_smooth'], label='Voltage vs. 1-SoC', color='red')
plt.title('Voltage vs. 1-SoC')
plt.xlabel('1-SoC')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()
