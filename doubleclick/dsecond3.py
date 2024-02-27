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
        sys.exit()

def read_interval_time(filename):
    try:
        with open(filename, 'r') as file:
            interval_time = int(file.read().strip())
            print(f"Interval time from {filename}: {interval_time}")
            return interval_time
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit()

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} file deleted successfully.")
    except OSError:
        print(f"Failed to delete file '{filename}'.")

def modify_interval(interval_time):
    modified_interval = (interval_time * 5) + 120
    print("Modified interval time:", modified_interval)
    return modified_interval

def click_continuous(x1 , y1, x2, y2 , interval_time):
    try:
        while True:
            for coord in coordinates:
                pyautogui.click(x1, y1)  # Click at the specified coordinates
                time.sleep(1)
                pyautogui.click(x2, y2)  # Click at the specified coordinates
                time.sleep(interval_time)  # Wait for the specified interval (in seconds)
                print(f'Clicked at {coord}, waited for {interval_time} sec')
                click_continuous(x1 , y1, x2, y2 , interval_time)
    except KeyboardInterrupt:
        print("Script terminated by user.")

def main():
    # Install required packages
    import pyautogui
    
    # Download count.txt file
    count_url = "https://raw.githubusercontent.com/ameenTheprogramer/imgcount/main/count.txt"
    download_file(count_url, 'count.txt')

    # Read the content of count.txt file
    interval_time = read_interval_time('count.txt')

    # Delete the count.txt file
    # delete_file('count.txt')

    # Modify the interval_time
    modified_interval = modify_interval(interval_time)

    # Define the coordinates
    #coordinates = [(83, 306), (747, 305)]
    crd1x = 83
    crd1y = 306
  
    crd2x = 747
    crd2y = 305

    # Click continuously at the specified coordinates with the modified interval
    click_continuous(crd1x, crd1y , crd2x , crd2y , modified_interval)

if __name__ == "__main__":
    main()
