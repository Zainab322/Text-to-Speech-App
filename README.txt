# Text-to-Speech Web App (Flask + pyttsx3)

## Summary
This app converts text to speech locally using pyttsx3. Users can type text or upload .txt/.pdf files, pick voice/rate/volume, and download the generated audio.

## Requirements
- Python 3.x (3.8+)
- pip

## Python dependencies
Install:
    pip install -r requirements.txt

Optional (for MP3 output):
- Install ffmpeg and ensure it's in PATH.
  - Windows: download from https://ffmpeg.org/download.html and add bin folder to PATH
  - Mac (Homebrew): `brew install ffmpeg`
  - Linux (apt): `sudo apt install ffmpeg`
- Install pydub (already in requirements.txt)

## Run (development)
1. Create venv (recommended):
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Start Flask:
   # Windows PowerShell
   $env:FLASK_APP = "app.py"
   flask run

   # Or run directly:
   python app.py

4. Open browser:
   http://127.0.0.1:5000/

## Notes & Troubleshooting
- `pyttsx3` uses platform TTS backends. On some Linux servers you might need additional packages (espeak, etc).
- MP3 conversion requires ffmpeg. If MP3 conversion fails, the app will return WAV.
- If voice list is empty or pyttsx3 fails, check your system TTS voices / drivers.
- For production/public deployment, do not use `debug=True`, and set a secure `app.secret_key`. Consider using a queued TTS job if many users will request audio.

## Future Work
- Add authentication & per-user file cleanup.
- Add progress bar while processing longer texts.
- Integrate Coqui (for natural voices) or cloud TTS (OpenAI/Deepgram) later if billing is available.
