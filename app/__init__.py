import json

def load_vocab():
    with open('data/vocab.json', 'r', encoding='utf-8') as file:
        return json.load(file)
