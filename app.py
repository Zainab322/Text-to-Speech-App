from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import pyttsx3
import os
import PyPDF2

app = Flask(__name__)
CORS(app)

OUTPUT_DIR = os.path.join("static", "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {'txt', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    voice = data.get("voice", "default")
    rate = int(data.get("rate", 200))
    volume = float(data.get("volume", 1.0))

    if not text.strip():
        return jsonify({"message": "No text provided", "url": None})

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if voice == "male":
        engine.setProperty('voice', voices[0].id)
    elif voice == "female" and len(voices) > 1:
        engine.setProperty('voice', voices[-1].id) 
    else:
        engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    filename = "speech.wav"
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        engine.save_to_file(text, filepath)
        engine.runAndWait()
    except Exception as e:
        return jsonify({"message": f"Error generating speech: {e}", "url": None})

    file_url = url_for('static', filename=f'audio/{filename}')
    return jsonify({"message": "Speech generated", "url": file_url})

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file uploaded", "text": ""})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file", "text": ""})

    if not allowed_file(file.filename):
        return jsonify({"message": "Only .txt and .pdf files are supported", "text": ""})

    text = ""
    try:
        if file.filename.endswith(".txt"):
            text = file.read().decode('utf-8')
        elif file.filename.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return jsonify({"message": f"Error reading file: {e}", "text": ""})

    return jsonify({"message": f"{file.filename} loaded successfully", "text": text})

if __name__ == "__main__":
    app.run(debug=True)
