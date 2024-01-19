# Open AI Voice Assiatant in Python
Simple voice assistant developed in Python that uses OpenAI's GPT-3 API for sound analysis and response generation, SoundDevice for recording audio, and pyttsx3 for text-to-speech conversion.

## Features
- **Voice Recording**: Records user's voice for 5 seconds 
- **Sound Analysis**: Leverages OpenAI's GPT-3 model for language analysis and generates a response in the user's natural language
- **T2S**: Converts the assistant's text responses into voice and speaks them out.


## Disclaimer
Note: This project is for educational purposes only. You can use it at your own risk. 
OpenAI API keys are secret and SHOULD NOT be exposed or saved to the public domain to avoid misuse. DO NOT COMMIT it to git.

## Cloning Repository 
First, clone this repository to your local machine using:

```
git clone https://github.com/marma-dev/openai-assistant.git
```

## Requirements
The following requirements should be present before running the assistant:  

- Python 3.7 or higher.
- OpenAI Python
- SoundDevice
- pyttsx3
- dotenv
- SciPy
- NumPy

Python can be installed from https://www.python.org/downloads

Install the dependencies (preferably from the folder containing the repo) using the following command
```
$ pip install <dependency-name>
```
e.g
```
$ pip install openai
```

## Usage Instructions
You'll need OpenAI API key to use the assistant. Create a OpenAI account if you don't have one yet.
The assistant script takes the key from dotenv using the .env file.
So create a .env file with the following content
```
OPENAI_API_KEY=<insert-your-OpenAI-API-key-here>
```

You can start the assistant by running the openai-assistant.py script:

```
python openai-assistant.py
```

The assistant will start listening to you. Chat away or say a command! (Psst! It listens for 5 seconds for every input from you, so keep it short ;) ). The assistant will leverage OpenAI GPT-3 model for language analysis and generate a response in your language. To stop the assistant, say "Close Assistant".


## Contribution & License Terms
This is currently licensed under the terms of the MIT license. 
Have a suggestion, or found a bug? Create an issue and we'll get on it!
All contributions are welcome!

