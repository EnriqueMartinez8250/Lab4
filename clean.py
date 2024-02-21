import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Path to your CSV file
csv_file_path = 'Data.csv'
# Read the CSV file
df = pd.read_csv(csv_file_path)

# Assuming the 'Time' column is in milliseconds and represents the total duration of your experiment
# Convert 'Time' to seconds if it's not already (adjust this based on your actual time unit)
df['Time_seconds'] = df['Time'] / 1000  # Adjust this line if your time unit is different

# Smooth the Voltage data using a rolling window
window_size = 50  # Adjust this based on your dataset for desired smoothness
df['Voltage_smooth'] = df['Voltage'].rolling(window=window_size, center=True).mean()

# Plotting both original and smoothed Voltage vs. Time
plt.figure(figsize=(12, 6))

# Original Voltage vs. Time
plt.plot(df['Time_seconds'], df['Voltage'], label='Original Voltage', alpha=0.5)

# Smoothed Voltage vs. Time
plt.plot(df['Time_seconds'], df['Voltage_smooth'], label='Smoothed Voltage', color='red')

plt.title('Voltage vs. Time (Original vs. Smoothed)')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()
