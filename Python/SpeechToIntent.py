import json
import pvrhino
from dotenv import load_dotenv
import os
import pyaudio
import numpy as np

load_dotenv()
API_KEY = os.getenv("API_KEY_3")

# Initialize Rhino with the provided API key and context
rhino = pvrhino.create(
    access_key=API_KEY,
    context_path='./Custom_Data/Custom_Context.rhn'
)

# Define the audio frame size and sampling rate for the microphone
FRAME_SIZE = 512  # Define the number of audio samples per frame
SAMPLE_RATE = 16000  # Rhino requires 16kHz audio samples

# Initialize the audio stream with pyaudio
p = pyaudio.PyAudio()

# Open the microphone stream
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=SAMPLE_RATE,
                input=True,
                frames_per_buffer=FRAME_SIZE)

def get_next_audio_frame():
    # Capture the next audio frame from the microphone
    audio_frame = np.frombuffer(stream.read(FRAME_SIZE), dtype=np.int16)
    return audio_frame

while True:
    # Get the next audio frame
    audio_frame = get_next_audio_frame()

    # Process the audio frame with Rhino
    is_finalized = rhino.process(audio_frame)
    
    if is_finalized:
        # Get inference when the audio frame is finalized
        inference = rhino.get_inference()
        
        if inference.is_understood:
            # If the inference was understood, process the intent and slots
            intent = inference.intent
            slots = inference.slots
            print(f"Intent: {intent}")
            print(f"Slots: {slots}")
            
            data = {
                "intent": intent,
                "slots": slots
            }
            with open("./.temp/intent_and_slots.json", "w") as f:
                json.dump(data, f)
            
            # Break the loop after the first intent is captured
            break
        else:
            print("No intent understood")

# Stop and close the audio stream, and terminate Rhino
stream.stop_stream()
stream.close()
p.terminate()
rhino.delete()  # Cleanly delete the Rhino instance

