import pyttsx3

def generate_speech(text, voice="female", rate=200, volume=1.0, pitch=50, filename="output.mp3"):
    engine = pyttsx3.init()

    # Set voice (male/female)
    voices = engine.getProperty("voices")
    if voice == "male":
        engine.setProperty("voice", voices[0].id)  # usually male
    else:
        engine.setProperty("voice", voices[1].id)  # usually female

    # Set rate (speed)
    engine.setProperty("rate", rate)

    # Set volume
    engine.setProperty("volume", volume)

    # Pitch is tricky in pyttsx3 (not directly supported everywhere),
    # some voices may ignore it, but we simulate with rate adjustments
    adjusted_rate = int(rate * (pitch / 50))  
    engine.setProperty("rate", adjusted_rate)

    engine.save_to_file(text, filename)
    engine.runAndWait()
