import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
csv_file_path = 'Data.csv'  # Update this path to where your CSV file is located
data = pd.read_csv(csv_file_path)

# Convert 'Time' from milliseconds to seconds
data['Time_s'] = data['Time'] / 1000  # Convert time to seconds
R_b = 0.5  
data['Current_Adjusted'] = data['Current'] / 1000  # Convert current from mA to A



# Adjust voltage for internal resistance
# This line assumes you want to perform this adjustment; otherwise, you can skip this calculation
data['Voltage_Adjusted'] = data['Voltage'] + data['Current_Adjusted'] * R_b 

# Plotting
plt.figure(figsize=(12, 6))

# Plot Original Voltage
#plt.plot(data['Time_s'], data['Voltage'], label='Original Voltage', marker='o', linestyle='-', markersize=4, color='blue')

# Plot Adjusted Voltage (if applicable)
plt.plot(data['Time_s'], data['Voltage_Adjusted'], label='Adjusted Voltage', marker='x', linestyle='--', markersize=4, color='red')

plt.xlabel('Time (seconds)')
plt.ylabel('Voltage (V)')
plt.title('Voltage vs. Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.xlim(200,600)

plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels


plt.show()
