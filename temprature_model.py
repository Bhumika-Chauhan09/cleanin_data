#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

# List files in the current directory
current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)
files_in_directory
get_ipython().run_line_magic('matplotlib', 'inline')
import sys
sys.version
import tkinter as tk
import csv
import time
import matplotlib.pyplot as plt
import pandas as pd  # Assuming you're using pandas to work with the CSV file

# Load the CSV file
# Use a raw string literal for the file path
csv_file = r'D:\Semester5\caspstone-SIT374\temp_data.csv'

# Function to check sensor data and generate alerts
def check_sensor_data():
    try:
        timestamps = []
        temperatures = []

        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            # Assuming the first row contains headers, skip it
            next(reader)

            # Read all temperature readings and timestamps
            for row in reader:
                timestamp, temperature = row
                timestamps.append(timestamp)
                temperature = float(temperature)
                temperatures.append(temperature)

        # Define the temperature limit for the alert
        temperature_limit = 23.89  # Adjust to your desired limit

        # Create a list to store alert readings
        alert_readings = []

        # Check if each temperature reading exceeds the limit
        for timestamp, temperature in zip(timestamps, temperatures):
            if temperature > temperature_limit:
                alert_readings.append((timestamp, temperature))

        if alert_readings:
            # Log the alert to the notebook output
            for timestamp, temperature in alert_readings:
                alert_message = f"Temperature Alert: {temperature}°C exceeds the limit of {temperature_limit}°C at {timestamp}."
                print(alert_message)

            # Create a plot to visualize all temperature readings
            plt.figure(figsize=(12, 6))
            plt.plot(timestamps, temperatures, 'bo-', label='Temperature Reading')
            
            # Highlight alert readings in red
            for timestamp, temperature in alert_readings:
                plt.plot(timestamp, temperature, 'ro', label='Alert Reading')

            plt.axhline(temperature_limit, color='r', linestyle='--', label='Temperature Limit')
            plt.xlabel('Timestamp')
            plt.ylabel('Temperature (°C)')
            plt.legend()
            plt.title('Temperature Alert')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")

# Run the periodic sensor data check
while True:
    check_sensor_data()
    # Adjust the sleep duration (in seconds) based on your project requirements
    time.sleep(60)  # Check every minute

