import pyautogui

def main():
    # Install required packages
    import pyautogui
    # Download count.txt file
    count_url = "https://raw.githubusercontent.com/ameenTheprogramer/imgcount/main/count.txt"
    download_file(count_url, 'count.txt')

    # Read the content of count.txt file
    interval_time = read_interval_time('count.txt')

    # Delete the count.txt file
    delete_file('count.txt')

    # Modify the interval_time
    modified_interval = modify_interval(interval_time)

    # Click continuously at the specified coordinates with the modified interval
    click_continuous(84, 302, modified_interval)


if __name__ == "__main__":
    main()
