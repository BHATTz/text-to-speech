https://bhattz.github.io/text-to-speech/templates/index.html

To create a Text-to-Speech (TTS) project in Python for a website, you'll need to use a combination of backend and frontend technologies. For the backend, you can use Python to handle the text-to-speech conversion, and for the frontend, you can use HTML, CSS, and JavaScript to build the user interface and handle the interactions with the backend. Below is an outline of the steps to achieve this:

1. Set up the project structure:
Create a directory for your project and organize it with the following files and folders:

```
- project_folder/
  - static/
    - styles.css
  - templates/
    - index.html
  - app.py
```

2. Install required libraries:
In your Python environment, install the necessary libraries using pip. For this project, you can use Flask to create a simple web server and gTTS (Google Text-to-Speech) to handle the text-to-speech conversion.

```
pip install Flask gTTS
```

3. Implement the backend (app.py):
In `app.py`, import the necessary modules and set up the Flask application.

```python
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
```

4. Create the frontend (index.html):
In `index.html`, create a simple web page with an input box, a button to trigger the TTS conversion, and an audio player to play the generated speech.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Text-to-Speech</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <h1>Text-to-Speech</h1>
    <textarea id="input-text" placeholder="Enter your text here..."></textarea>
    <button id="convert-btn">Convert to Speech</button>
    <audio id="audio-player" controls></audio>

    <script>
        document.getElementById('convert-btn').addEventListener('click', function () {
            const text = document.getElementById('input-text').value;
            fetch('/tts', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const audioPlayer = document.getElementById('audio-player');
                    audioPlayer.src = '/static/output.mp3';
                    audioPlayer.play();
                }
            });
        });
    </script>
</body>
</html>
```

5. Add CSS styles (styles.css):
You can create a `styles.css` file in the `static` folder to style the web page as you like.

6. Run the application:
Save all the files and run the Flask app by executing `python app.py`. The application will start, and you can access it by visiting `http://127.0.0.1:5000/` in your web browser.

Now, when you enter text into the input box and click the "Convert to Speech" button, the text will be sent to the server, converted to speech, and played back using an audio player on the web page. Remember that this example uses gTTS, which requires an internet connection to access Google's TTS service.
