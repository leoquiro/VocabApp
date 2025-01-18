# Hindi Vocabulary App Backend

This is the backend for the Hindi Vocabulary App. It provides APIs for vocabulary data, answer checking, and text-to-speech functionality.

## Features

- Serve vocabulary data via RESTful APIs.
- Check the user's input and provide feedback.
- Use text-to-speech to pronounce the displayed word.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/hindi-vocab-app-backend.git
    cd hindi-vocab-app-backend
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

## Usage

1. Run the backend server:
    ```sh
    python app.py
    ```

2. The backend server will be available at `http://localhost:5000`.

## API Endpoints

- `GET /api/vocab`: Fetch vocabulary data.
- `GET /api/random-word?category=<category>`: Fetch a random word from the specified category.
- `POST /api/check-answer`: Check if the user's answer is correct.
- `POST /api/speak-word`: Generate and return the audio for a word.

## File Structure

- [app.py](app.py): Entry point of the backend application.
- [app](app): Contains the main application logic.
  - [__init__.py](app/__init__.py): Loads the vocabulary from the JSON file.
  - [logic.py](app/logic.py): Contains functions for selecting random words and checking answers.
  - [speech.py](app/speech.py): Contains functions for speech recognition.
  - [tts.py](app/tts.py): Contains functions for text-to-speech.
- [assets](assets): Contains assets such as fonts.
- [data](data): Contains data files such as the vocabulary JSON file.

## Dependencies

- Flask
- Flask-Cors
- gTTS
- pygame

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [gTTS](https://pypi.org/project/gTTS/)
- [pygame](https://www.pygame.org/)