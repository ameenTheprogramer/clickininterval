import os
import requests
import subprocess

def check_and_delete_files():
    current_dir = os.getcwd()
    clickwithinterval4_path = os.path.join(current_dir, 'clickwithinterval4.py')
    second_py_path = os.path.join(current_dir, 'second.py')

    if os.path.exists(clickwithinterval4_path):
        os.remove(clickwithinterval4_path)
        print("Deleted clickwithinterval4.py")

    if os.path.exists(second_py_path):
        os.remove(second_py_path)
        print("Deleted second.py")

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

def main():
    # Check and delete existing files
    check_and_delete_files()

    # Download clickwithinterval4.py
    url = "https://github.com/ameenTheprogramer/clickininterval/raw/main/clickwithinterval4.py"
    filename = "clickwithinterval4.py"
    download_file(url, filename)

if __name__ == "__main__":
    main()
    subprocess.run(['python', 'clickwithinterval4.py'])
