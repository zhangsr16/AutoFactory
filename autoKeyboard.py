import pyautogui
import time
import subprocess

def open_notepad():
    # Open Notepad using subprocess
    subprocess.Popen('notepad.exe')
    time.sleep(2)  # Wait for Notepad to open

def write_text_in_notepad():
    # Write text in Notepad using pyautogui
    pyautogui.typewrite("Hello, this is an automated message.", interval=0.1)
    pyautogui.press('enter')
    pyautogui.typewrite("This message was typed by a Python script!", interval=0.1)

def save_file():
    # Simulate Ctrl+S to open the Save dialog
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)  # Wait for the Save dialog to open
    
    # Type the file name and save
    pyautogui.typewrite("automated_note.txt")
    pyautogui.press('enter')
    time.sleep(1)  # Wait for the file to save

def run_command():
    # Example of running a command-line operation
    result = subprocess.run(['echo', 'Hello from the command line!'], capture_output=True, text=True)
    print(result.stdout)

def main():
    open_notepad()
    write_text_in_notepad()
    save_file()
    run_command()

if __name__ == "__main__":
    main()
