<<<<<<< HEAD
import pyttsx3
import os

# Initialize TTS engine
engine = pyttsx3.init()

# Configure voice properties
engine.setProperty("rate", 150)     # Speed of speech (default ~200)
engine.setProperty("volume", 1.0)   # Volume (0.0 to 1.0)

# Choose voice (male/female depending on system voices)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # voices[0] = male, voices[1] = female (usually)

# Create output folder if not exists
output_folder = "output_audio"
os.makedirs(output_folder, exist_ok=True)

# Text to convert
text = "Hello! This is my first text to speech assignment using Python and pyttsx3."

# Save output file
output_path = os.path.join(output_folder, "speech.wav")
engine.save_to_file(text, output_path)

# Run and generate
engine.runAndWait()

print(f"✅ Audio generated successfully! Check '{output_path}'")
=======
import pyttsx3
import os

# Initialize TTS engine
engine = pyttsx3.init()

# Configure voice properties
engine.setProperty("rate", 150)     # Speed of speech (default ~200)
engine.setProperty("volume", 1.0)   # Volume (0.0 to 1.0)

# Choose voice (male/female depending on system voices)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # voices[0] = male, voices[1] = female (usually)

# Create output folder if not exists
output_folder = "output_audio"
os.makedirs(output_folder, exist_ok=True)

# Text to convert
text = "Hello! This is my first text to speech assignment using Python and pyttsx3."

# Save output file
output_path = os.path.join(output_folder, "speech.wav")
engine.save_to_file(text, output_path)

# Run and generate
engine.runAndWait()

print(f"✅ Audio generated successfully! Check '{output_path}'")
>>>>>>> 181461fe646f42beebf56fa590fbd6e51246efa5
