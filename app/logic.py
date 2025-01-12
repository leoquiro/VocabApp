import random

def select_random_word(vocab):
    """Randomly select a word and determine whether to show the Hindi or English version."""
    selected = random.choice(vocab)
    if random.choice([True, False]):
        # Show the Hindi word and expect the English meaning
        return selected["hindi"], selected["english"].strip().lower()
    else:
        # Show the English word and expect the Hindi meaning
        return selected["english"], selected["hindi"].strip().lower()

def check_answer(user_input, correct_meaning):
    """Check if the entered meaning is correct."""
    return user_input == correct_meaning