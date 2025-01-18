from flask import Flask, request, jsonify
from flask_cors import CORS
from app import load_vocab
from app.logic import select_random_word, check_answer
from app.tts import speak_word

app = Flask(__name__)
CORS(app)

vocab_data = load_vocab()

@app.route('/api/vocab', methods=['GET'])
def get_vocab():
    return jsonify(vocab_data)

@app.route('/api/random-word', methods=['GET'])
def get_random_word():
    category = request.args.get('category')
    if category not in vocab_data['categories']:
        return jsonify({'error': 'Invalid category'}), 400
    word, meaning = select_random_word(vocab_data['categories'][category])
    return jsonify({'word': word, 'meaning': meaning})

@app.route('/api/check-answer', methods=['POST'])
def api_check_answer():
    data = request.json
    user_input = data.get('user_input')
    correct_meaning = data.get('correct_meaning')
    if not user_input or not correct_meaning:
        return jsonify({'error': 'Invalid input'}), 400
    is_correct = check_answer(user_input, correct_meaning)
    return jsonify({'correct': is_correct})

@app.route('/api/speak-word', methods=['POST'])
def api_speak_word():
    data = request.json
    word = data.get('word')
    if not word:
        return jsonify({'error': 'Invalid input'}), 400
    speak_word(word)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)