import pyautogui
import time
from pywinauto import application

# Function to open an application
def open_application(path):
    app = application.Application().start(path)
    return app

# Function to automate GUI operations using pyautogui
def automate_gui_operations():
    # Wait for the application to open
    time.sleep(5)
    
    # Example: Move mouse to a specific position and click
    pyautogui.moveTo(100, 200)
    pyautogui.click()
    
    # Example: Type some text
    pyautogui.typewrite("Hello, World!")
    
    # Example: Press a key
    pyautogui.press("enter")

def main():
    # Path to the application executable
    app_path = "C:\\Path\\To\\Application.exe"
    
    # Open the application
    open_application(app_path)
    
    # Perform automated GUI operations
    automate_gui_operations()

if __name__ == "__main__":
    main()
