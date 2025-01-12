from gtts import gTTS
import pygame
import io

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def speak_word(word):
    """Speak a given word using Google TTS and pygame."""
    tts = gTTS(text=word, lang="hi")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    # Load the in-memory audio into pygame
    pygame.mixer.music.load(audio_data, "mp3")
    pygame.mixer.music.play()

    # Wait until the audio finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
