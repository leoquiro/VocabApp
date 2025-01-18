from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from app.ui import QuizWordDisplay
from app.__init__ import load_vocab

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.title = Label(text="Select a Category", font_size=32, size_hint=(1, 0.2))
        self.layout.add_widget(self.title)

        self.categories = load_vocab()["categories"]
        for category in self.categories:
            button = MDRaisedButton(
                text=category.capitalize(),
                size_hint=(1, None),
                height=50
            )
            button.bind(on_press=self.load_category)
            self.layout.add_widget(button)

    def load_category(self, instance):
        category = instance.text.lower()
        self.manager.current = 'quiz'
        self.manager.get_screen('quiz').load_words(self.categories[category])

class QuizScreen(Screen, QuizWordDisplay):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(QuizWordDisplay())

    def load_words(self, words):
        self.children[0].vocab = words
        self.children[0].show_random_word()

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menu_screen = MenuScreen(name='menu')
        self.quiz_screen = QuizScreen(name='quiz')
        self.add_widget(self.menu_screen)
        self.add_widget(self.quiz_screen)

class HindiVocabApp(MDApp):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    HindiVocabApp().run()