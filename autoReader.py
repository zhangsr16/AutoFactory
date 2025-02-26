import pyttsx3

def read_text_file(file_path):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Open and read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Set properties for the TTS engine
    engine.setProperty('rate', 250)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Use the TTS engine to say the text
    engine.say(text)

    # Wait for the TTS engine to finish speaking
    engine.runAndWait()


file_path = 'Read4.txt'  # Replace with your txt file path
read_text_file(file_path)
