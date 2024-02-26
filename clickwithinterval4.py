import subprocess
import requests
import os
import time
import sys

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def run_with_confirmation(command):
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    process.communicate(b'y\n')

def xserver():
    # Get the value of $DISPLAY
    display = subprocess.run("echo $DISPLAY", shell=True, capture_output=True, text=True)
    display_value = display.stdout.strip()

    # Create .Xauthority file and set permissions
    run_command("touch ~/.Xauthority")
    run_command("chmod 600 ~/.Xauthority")

    # Export DISPLAY=:0
    run_command(f"export DISPLAY={display_value}")

def install_packages():
    subprocess.run(["apt", "update"])
    run_with_confirmation(['sudo', 'apt-get', 'install', 'xterm'])
    run_with_confirmation(['sudo', 'apt', 'install', '-y', 'python3-pip'])
    subprocess.run(['pip3', 'install', '--upgrade', 'pip'])
    subprocess.run(['pip3', 'install', 'pynput'])
    subprocess.run(['pip3', 'install', 'pyautogui'])
    run_with_confirmation(['sudo', 'apt-get', 'install', 'python3-tk', 'python3-dev'])
    subprocess.run(['wget', 'https://raw.githubusercontent.com/ameenTheprogramer/clickininterval/main/2nd.py'])




# def open_xterm_and_execute_script(script_name):
#     command = f'python {script_name}'
#     subprocess.Popen(['xterm', '-e', command])

# def run2nd():
#     script_name = '2nd.py'
#     open_xterm_and_execute_script(script_name)






# def download_file(url, filename):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(filename, 'wb') as f:
#             f.write(response.content)
#     else:
#         print(f"Failed to download {filename} file.")
#         sys.exit()

# def read_interval_time(filename):
#     try:
#         with open(filename, 'r') as file:
#             interval_time = int(file.read().strip())
#             print(f"Interval time from {filename}: {interval_time}")
#             return interval_time
#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         sys.exit()

# def delete_file(filename):
#     try:
#         os.remove(filename)
#         print(f"{filename} file deleted successfully.")
#     except OSError:
#         print(f"Failed to delete file '{filename}'.")

# def modify_interval(interval_time):
#     modified_interval = (interval_time * 5) + 120
#     print("Modified interval time:", modified_interval)
#     return modified_interval

# def click_continuous(x, y, interval_time):
#     try:
#         while True:
#             pyautogui.click(x, y)  # Click at the specified coordinates
#             time.sleep(interval_time / 1000)  # Wait for the specified interval
#     except KeyboardInterrupt:
#         print("Script terminated by user.")

# def main():
#     import pyautogui
#     # Download count.txt file
#     count_url = "https://raw.githubusercontent.com/ameenTheprogramer/imgcount/main/count.txt"
#     download_file(count_url, 'count.txt')

#     # Read the content of count.txt file
#     interval_time = read_interval_time('count.txt')

#     # Delete the count.txt file
#     delete_file('count.txt')

#     # Modify the interval_time
#     modified_interval = modify_interval(interval_time)

#     # Click continuously at the specified coordinates with the modified interval
#     click_continuous(84, 302, modified_interval)

if __name__ == "__main__":
    install_packages()
    xserver()
    subprocess.Popen(['xterm', '-e', 'python 2nd.py'])
    # main()
