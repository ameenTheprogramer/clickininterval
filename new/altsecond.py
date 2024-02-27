import pyautogui
import requests
import os
import time
import sys

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print(f"Failed to download {filename} file.")
        sys.exit(1)

def read_interval_time(filename):
    try:
        with open(filename, 'r') as file:
            interval_time = int(file.read().strip())
            print(f"Interval time from {filename}: {interval_time}")
            return interval_time
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)

def modify_interval(interval_time):
    modified_interval = (interval_time * 5) + 120
    print("Modified interval time:", modified_interval)
    return modified_interval

def click_continuous(x, y, interval_time):
    try:
        while True:
            pyautogui.click(x, y)  # Click at the specified coordinates
            print(f'Waited for {interval_time} sec')
            time.sleep(interval_time)  # Wait for the specified interval (in seconds)
            click_continuous(x, y, interval_time)
    except KeyboardInterrupt:
        print("Script terminated by user.")

def main():
    # Download the configuration file
    config_url = "https://raw.githubusercontent.com/ameenTheprogramer/imgcount/main/altcount.txt"
    download_file(config_url, 'altcount.txt')

    # Read the interval time from the configuration file
    interval_time = read_interval_time('altcount.txt')

    # Modify the interval time
    modified_interval = modify_interval(interval_time)

    # Click continuously at the specified coordinates with the modified interval
    click_continuous(84, 302, modified_interval)

if __name__ == "__main__":
    main()
