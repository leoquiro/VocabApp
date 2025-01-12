# Hindi Vocabulary App

This is a Hindi Vocabulary App built using Kivy and KivyMD. The app helps users learn Hindi vocabulary by displaying words in Hindi or English and asking the user to provide the correct translation. The app also supports speech recognition and text-to-speech functionality.

## Features

- Display random Hindi or English words and ask for the correct translation.
- Check the user's input and provide feedback.
- Use speech recognition to listen for the user's spoken input.
- Use text-to-speech to pronounce the displayed word.
- Customizable UI with Kivy and KivyMD.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hindi-vocab-app.git
    cd hindi-vocab-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Ensure you have the necessary system dependencies for [pygame](http://_vscodecontentref_/0) and [speech_recognition](http://_vscodecontentref_/1).

## Usage

1. Run the app:
    ```sh
    python main.py
    ```

2. The app will display a random word in Hindi or English. Enter the correct translation in the text input field and press "Submit".

3. Use the "Speak" button to hear the pronunciation of the displayed word.

4. Use the "Repeat" button to hear the pronunciation again.

5. The app will provide feedback on whether the entered translation is correct or not.

## File Structure

- [main.py](http://_vscodecontentref_/2): Entry point of the application.
- [app](http://_vscodecontentref_/3): Contains the main application logic.
  - [__init__.py](http://_vscodecontentref_/4): Loads the vocabulary from the JSON file.
  - [logic.py](http://_vscodecontentref_/5): Contains functions for selecting random words and checking answers.
  - [speech.py](http://_vscodecontentref_/6): Contains functions for speech recognition.
  - [tts.py](http://_vscodecontentref_/7): Contains functions for text-to-speech.
  - [ui.py](http://_vscodecontentref_/8): Contains the UI layout and logic.
- [assets](http://_vscodecontentref_/9): Contains assets such as fonts.
- [data](http://_vscodecontentref_/10): Contains data files such as the vocabulary JSON file.

## Dependencies

- Kivy
- KivyMD
- SpeechRecognition
- gTTS
- pygame

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Kivy](https://kivy.org/)
- [KivyMD](https://kivymd.readthedocs.io/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [gTTS](https://pypi.org/project/gTTS/)
- [pygame](https://www.pygame.org/)
