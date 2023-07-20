from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    text = data['text']
    tts = gTTS(text=text, lang='en')  # Adjust the language if needed
    tts.save('static/output.mp3')
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
