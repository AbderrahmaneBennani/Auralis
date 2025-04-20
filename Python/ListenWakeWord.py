from dotenv import load_dotenv
import os
import pvporcupine
import pyaudio
import subprocess
import random

load_dotenv()
API_KEY = os.getenv("PICO_API_KEY")

# Initialize Porcupine with the custom wake word
porcupine = pvporcupine.create(access_key=API_KEY, keyword_paths=['./Custom_Data/Custom_Keyword.ppn'])

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16, channels=1, rate=16000,
                 input=True, frames_per_buffer=porcupine.frame_length)

print("Listening for wake word...")

try:
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = [int.from_bytes(pcm[i:i+2], 'little', signed=True) for i in range(0, len(pcm), 2)]
        result = porcupine.process(pcm)
        if result >= 0:
            print("Wake word detected!")
            file_number = random.randint(1, 4)
            file_path = f"../Voice/Ready/{file_number}.wav"
            subprocess.run(["aplay", file_path])
            break

finally:
    stream.close()
    pa.terminate()
    porcupine.delete()

