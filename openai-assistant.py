import openai
import sounddevice
import numpy
from scipy.io import wavfile
import tempfile
import pyttsx3
from dotenv import load_dotenv
import os
class OpenAIAssitant:
    """
    This class represents OpenAI GPT-3 based voice assistant.
        
    Methods:
        hear: Listens to user by recording user voice/audio & transcribes it.
        process: Query OpenAI to process user input and respond.
        talk: Converts the response to speech and plays it.
    """
    load_dotenv()
    
    def __init__(self):
        # Set your OpenAI API key
        openai.api_key = os.getenv("OPENAI_API_KEY")
        # Initialize the assistant's history
        self.history = [
                {"role": "system", "content": "You are a user assistant. The user can speak to you in any language. You speak in the same language as user."}
            ]
        
    def hear(self):
        """
        Listens to user by recording user voice/audio & transcribes it.t for further processing
        """
        print("Listening to you...")
        
        #Setting parameters for recording
        duration = 5  # Record for 5 seconds
        samplefrequency = 44100  # Sample rate

        # Record the audio
        audio = sounddevice.rec(int(duration * samplefrequency), samplerate=samplefrequency, channels=1, dtype=numpy.int16)
        sounddevice.wait()

        # Save the NumPy array to a temporary wav file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            wavfile.write(temp_audio.name, samplefrequency, audio)

            # Transcribe the temporary audio file using OpenAI Whisper-1
            transcript = openai.Audio.transcribe("whisper-1", temp_audio)

        print(f"User: {transcript['text']}")
        return transcript['text']

    def process(self, text):
        """
        Query OpenAI to process user input and respond.
        """
        # Add the user's input to the assistant's history
        self.history.append({"role": "user", "content": text})
        # Send the conversation to the GPT-3.5 Turbo API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.history,
            temperature=0.5
        )
        # Extract the assistant's response from the API response
        response = dict(response.choices[0])['message']['content']
        self.history.append({"role": "system", "content": response})
        print('Assistant: ', response)
        return response

    def talk(self, text):
        """"
        Text to Speech convertion using PY TTS X3
        """
        # Initialize the speech engine
        engine = pyttsx3.init()

        # Convert text to speech
        engine.say(text)

        # Block while processing all currently queued commands
        engine.runAndWait()


if __name__ == "__main__":
    assistant = OpenAIAssitant()

    while True:
        command = assistant.hear()

        if "close assistant" in command.strip().lower():
            print("Assistant: Closing Assistant. Good Bye!")
            assistant.talk("Closing Assistant. Good Bye!")
            break
        
        response = assistant.process(command)
        assistant.talk(response)
