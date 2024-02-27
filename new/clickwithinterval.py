import subprocess

# Install necessary packages
subprocess.run(["pip", "install", "pyautogui"])

import time
import pyautogui

# Read interval time from file
with open('intervaltime.txt', 'r') as file:
    interval_time = int(file.read().strip())
    print(interval_time)
  
# Function to click on specific coordinates
def click_coordinates(x, y):
    pyautogui.click(x, y)

# Main function
def main():
    try:
        while True:
            click_coordinates(84, 302)
            time.sleep(interval_time / 1000)  # Convert milliseconds to seconds
    except KeyboardInterrupt:
        print("Stopping script")

if __name__ == "__main__":
    main()
