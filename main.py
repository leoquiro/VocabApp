from kivymd.app import MDApp
from app.menu import MyScreenManager

class HindiVocabApp(MDApp):
    def build(self):
        return MyScreenManager()

if __name__ == '__main__':
    HindiVocabApp().run()
