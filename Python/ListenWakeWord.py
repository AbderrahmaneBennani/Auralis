from dotenv import load_dotenv
import os
import pvporcupine
import pyaudio
import subprocess

load_dotenv()
API_KEY = os.getenv("API_KEY_3")

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
            subprocess.run(["aplay", "../Voice/Ready/1.wav"])
            break

finally:
    stream.close()
    pa.terminate()
    porcupine.delete()

