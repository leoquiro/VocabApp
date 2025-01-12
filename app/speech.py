import speech_recognition as sr
from app.logic import check_answer

def listen_for_word(correct_meaning):
    """Listen for user input and check if it matches the correct meaning."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            spoken_word = recognizer.recognize_google(audio).strip().lower()
            print(f"User said: {spoken_word}")
            if check_answer(spoken_word, correct_meaning):
                return True, spoken_word, correct_meaning, "Correct!"
            else:
                return False, spoken_word, correct_meaning, "Incorrect. Try again."
        except sr.UnknownValueError:
            return False, "Sorry, I did not understand."
        except sr.RequestError as e:
            return False, f"Speech recognition service error: {e}"