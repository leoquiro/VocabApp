from kivymd.app import MDApp
from app.ui import build_layout

class HindiVocabApp(MDApp):
    def build(self):
        return build_layout()

if __name__ == '__main__':
    HindiVocabApp().run()
