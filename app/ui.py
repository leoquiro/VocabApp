from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.clock import Clock
from app.__init__ import load_vocab
from app.tts import speak_word
from app.logic import select_random_word, check_answer
from app.speech import listen_for_word

class QuizWordDisplay(BoxLayout):
    current_word = StringProperty("")
    correct_meaning = StringProperty("")
    category_title = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.vocab = []  # Initialize with an empty list
        self.font_path = "assets/NotoSansDevanagari-VariableFont_wdth,wght.ttf"

        # Set background color to gray
        with self.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Light gray color
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

        # Category Title Label
        self.category_label = Label(
            text=self.category_title,
            font_size=32,
            halign="center",
            valign="middle",
            size_hint=(1, 0.2),
        )
        self.add_widget(self.category_label)

        # Top layout for word and repeat button
        top_layout = AnchorLayout(anchor_x="right", size_hint=(1, 0.6))

        # Word Label
        self.word_label = Label(
            text="",
            font_name=self.font_path,
            font_size=64,
            halign="center",
            valign="middle",
            size_hint=(1, 1),
        )
        top_layout.add_widget(self.word_label)

        # Repeat Button
        self.repeat_button = MDIconButton(
            icon="reload",
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={"right": 1, "top": 1}
        )
        self.repeat_button.bind(on_press=self.repeat_word)
        top_layout.add_widget(self.repeat_button)

        # Add top layout to main layout
        self.add_widget(top_layout)

        # Hint Button
        self.hint_button = MDRaisedButton(
            text="Hint",
            font_size=24,
            size_hint=(0.7, None),  # 70% width
            height=50,  # Fixed height
            pos_hint={"center_x": 0.5},  # Center horizontally
            md_bg_color=(0.2, 0.6, 0.86, 1),  # Custom background color
        )
        self.hint_button.bind(on_press=self.show_hint)
        self.add_widget(self.hint_button)

        # Text Input for Meaning
        input_layout = BoxLayout(
            size_hint=(1, None),
            height=50,
            padding=[self.width * 0.15, 50, self.width * 0.15, 50],
        )
        self.input_field = TextInput(
            hint_text="Enter the meaning...",
            font_size=24,
            multiline=False,
            size_hint=(0.7, None),  
            height=50,
            foreground_color=(1, 1, 1, 1),
            padding=[10, 10, 10, 10],  
            background_color=(0.1, 0.1, 0.1, 1),  
            background_normal='', 
            background_active='',  
            border=(45, 45, 45, 45)
        )
        input_layout.add_widget(self.input_field)
        self.add_widget(input_layout)

        # Submit Button
        submit_button_layout = BoxLayout(
            size_hint=(1, 0.2),
            padding=[self.width * 0.15, 0, self.width * 0.15, 0]  # 70% width, centered
        )
        self.submit_button = MDRaisedButton(
            text="Submit",
            font_size=24,
            size_hint=(0.7, None),  # 70% width
            height=50,  # Fixed height
            pos_hint={"center_x": 0.5},  # Center horizontally
            md_bg_color=(0.2, 0.6, 0.86, 1),  # Custom background color
        )
        self.submit_button.bind(on_press=self.check_answer)
        submit_button_layout.add_widget(self.submit_button)
        self.add_widget(submit_button_layout)

        # Speak Button
        speak_button_layout = BoxLayout(
            size_hint=(1, 0.2),
            padding=[self.width * 0.15, 0, self.width * 0.15, 0]  # 70% width, centered
        )
        self.speak_button = MDRaisedButton(
            text="Speak",
            font_size=24,
            size_hint=(0.7, None),  # 70% width
            height=50,  # Fixed height
            pos_hint={"center_x": 0.5},  # Center horizontally
            md_bg_color=(0.2, 0.6, 0.86, 1),  # Custom background color
        )
        self.speak_button.bind(on_press=self.listen_for_word)
        speak_button_layout.add_widget(self.speak_button)
        self.add_widget(speak_button_layout)

        # Feedback Label
        self.feedback_label = Label(
            text="",
            font_size=24,
            color=(0, 1, 0, 1),  # Default to green text
            size_hint=(1, 0.1)
        )
        self.add_widget(self.feedback_label)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        self.input_field.pos = (self.width * 0.15, self.input_field.y)
        self.input_field.size = (self.width * 0.7, 50)

    def show_random_word(self, dt=None):
        """Randomly select a new word, update the display, and speak it."""
        if not self.vocab:
            return
        self.current_word, self.correct_meaning = select_random_word(self.vocab)
        self.word_label.text = self.current_word
        self.input_field.text = ""
        self.feedback_label.text = "" 

        # Schedule the word to be spoken after a delay
        Clock.schedule_once(self.speak_current_word, 1)  # 1-second delay

    def speak_current_word(self, dt=None):
        """Speak the current word."""
        speak_word(self.current_word)

    def check_answer(self, *args):
        """Check if the entered meaning is correct."""
        user_input = self.input_field.text.strip().lower()
        if check_answer(user_input, self.correct_meaning):
            self.feedback_label.text = "Correct!"
            self.feedback_label.color = (0, 1, 0, 1)  # Green
            Clock.schedule_once(self.show_random_word, 1)  # Delay of 1 second
        else:
            self.feedback_label.text = "Try Again!"
            self.feedback_label.color = (1, 0, 0, 1)  # Red

    def listen_for_word(self, *args):
        """Listen for the spoken word and check if it is correct."""
        # Determine the language based on the current word
        if any(word["hindi"] == self.current_word for word in self.vocab):
            language = "en"
        else:
            language = "hi"
        
        success, message = listen_for_word(self.correct_meaning, language)
        self.feedback_label.text = message
        self.feedback_label.color = (0, 1, 0, 1) if success else (1, 0, 0, 1)
        if success:
            Clock.schedule_once(self.show_random_word, 1)  # Delay of 1 second

    def repeat_word(self, *args):
        speak_word(self.current_word)

    def show_hint(self, *args):
        """Show the meaning of the current word in the other language."""
        self.feedback_label.text = self.correct_meaning
        self.feedback_label.color = (0, 0, 1, 1)  # Blue

    def load_words(self, words, category_title):
        """Load a new set of words and display the first one."""
        self.vocab = words
        self.category_title = category_title
        self.category_label.text = category_title
        self.show_random_word()

def build_layout():
    return QuizWordDisplay()