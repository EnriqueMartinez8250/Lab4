import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file_path = 'Data.csv'
df = pd.read_csv(csv_file_path)

# Assuming the 'Time' column exists and represents elapsed time in seconds
# If your 'Time' column is not in seconds, adjust accordingly
df['Time_seconds'] = df['Time'] / 1000  # Adjust this if necessary

# Calculate SoC assuming it linearly decreases from 100% to 0% during the discharge
total_time = df['Time_seconds'].max()  # Total duration of the experiment
df['SoC'] = 1 - (df['Time_seconds'] / total_time)
df['1-SoC'] = 1 - df['SoC']
R = 0.05  


df['Voltage_compensated'] = df['Voltage'] + df['Current'] * R

window_size = 50  
df['Voltage_smooth'] = df['Voltage'].rolling(window=window_size, center=True).mean()
df['Voltage_compensated_smooth'] = df['Voltage_compensated'].rolling(window=window_size, center=True).mean()

# Plotting both original and compensated Voltage vs. 1-SoC
plt.figure(figsize=(12, 6))
plt.plot(df['1-SoC'], df['Voltage_smooth'], label='Original Voltage', color='blue', alpha=0.7)
plt.plot(df['1-SoC'], df['Voltage_compensated_smooth'], label='Compensated Voltage', color='red', linestyle='--', alpha=0.7)

plt.title('Voltage vs. 1-SoC')
plt.xlabel('1-SoC')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()
