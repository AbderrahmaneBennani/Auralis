#!/usr/bin/env python3
from dotenv import load_dotenv
import os
import subprocess
import pyttsx3
from openai import OpenAI


load_dotenv()
API_KEY = os.getenv("API_KEY_1")

client = OpenAI(
  api_key=API_KEY
)

def Record_Audio(input_path):
    """ Record a 3 second audio and overwrite the file """

    command = [
        'arecord',
        '-d', '3',
        '-r', '48000',
        '-c', '2',
        '-f', 'S16_LE',
        input_path
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(command)
        # If there was an error, print it to stderr
        if result.stderr:
            print(f"Error: {result.stderr}")
        
        print("3-Second Audio has been Recorded.")    

    except Exception as e:
        print(f"Error running recording the audio: {str(e)}")
    
def Speech_To_Text(input_path):
    """
    Runs whisper-cli with a hardcoded audio file path and prints the output.
    """
    
    command = [
        '../Whisper/Scripts/whisper-cli',
        '-m', '../Whisper/Models/ggml-tiny.en.bin',
        input_path,
        '--no-prints',
        '--no-timestamps'
    ]
    
    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        Text = result.stdout.strip()
        
        print("Speech has been convereted to Text")   
        # If there was an error, print it to stderr
        if result.stderr:
            print(f"Error: {result.stderr}")
            
        return Text
        
    except Exception as e:
        print(f"Error running whisper-cli: {str(e)}")
        return 1
    
def get_openai_response(query):
    try:
        completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": query}
  ]
)
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return None
    
def  Text_To_Speech(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    print("Response has been convereted to Speech.")

def Play_Audio(output_path):
    """ Play the response audio """

    command = [
        'aplay',
        output_path
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(command)
        # If there was an error, print it to stderr
        if result.stderr:
            print(f"Error: {result.stderr}")
        
        print("Audio is playing..")    

    except Exception as e:
        print(f"Error running recording the audio: {str(e)}")


if __name__ == "__main__":
    input_path = "../.temp/audio/input.wav"
    output_path = "../.temp/audio/output.wav"
    Record_Audio(input_path)
    query = Speech_To_Text(input_path)
    print("Query:", query)
    response = get_openai_response(query)
    print("Response:",get_openai_response(query))
    Text_To_Speech(response, output_path)
    Play_Audio(output_path)
    print("Program is done. Exit.")