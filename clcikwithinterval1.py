import subprocess
import requests
import os
import time
import pyautogui
import sys

# Install required packages
subprocess.run(["pip", "install", "requests", "pyautogui"])

# Download count.txt file
count_url = "https://raw.githubusercontent.com/ameenTheprogramer/imgcount/main/count.txt"
response = requests.get(count_url)
if response.status_code == 200:
    with open('count.txt', 'wb') as f:
        f.write(response.content)
else:
    print("Failed to download count.txt file.")
    sys.exit()

# Get the absolute path of the directory where the script is located
script_dir = os.getcwd()  # Current working directory
print("Script directory:", script_dir)

# Define the path to the count.txt file
count_file = os.path.join(script_dir, 'count.txt')
print("Count file path:", count_file)

# Read the content of count.txt file
try:
    with open(count_file, 'r') as file:
        interval_time = int(file.read().strip())
        print("Interval time from count.txt:", interval_time)
except FileNotFoundError:
    print(f"File '{count_file}' not found.")

# Delete the count.txt file
try:
    os.remove(count_file)
    print("count.txt file deleted successfully.")
except OSError:
    print(f"Failed to delete file '{count_file}'.")

# Modify the interval_time
interval_time = (interval_time * 5) + 120
print("Modified interval time:", interval_time)

# Main loop for continuous clicking
try:
    while True:
        pyautogui.click(84, 302)  # Click at the specified coordinates
        time.sleep(interval_time / 1000)  # Wait for the specified interval
except KeyboardInterrupt:
    print("Script terminated by user.")
