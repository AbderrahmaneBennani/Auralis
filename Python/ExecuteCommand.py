import json
import subprocess
import os

def execute_command(intent, slots):
    if intent == "toggleMusic":
        toggle_action = slots.get("toggle")

        if toggle_action == "play":
            print("🎶 Playing music...")

            # Launch music in background using aplay (non-blocking)
            music_file = "../Media/music.wav"  # Update path to your file
            try:
                subprocess.Popen(["aplay", music_file])
                print("✅ Music playback started.")
            except FileNotFoundError:
                print("❌ Could not find aplay or the music file.")

            # Relaunch main.py to go back to wake-word listening
            try:
                print("🔁 Relaunching main.py to listen for wake word...")
                subprocess.Popen(["python3", "main.py"])
            except FileNotFoundError:
                print("❌ Could not find main.py.")

        elif toggle_action == "stop":
            print("⏹️ Stopping music...")
            # Kill all aplay processes (or replace with smarter PID tracking)
            subprocess.call(["pkill", "-f", "aplay"])
            print("✅ Music stopped.")

            # Relaunch main.py to go back to wake-word listening
            try:
                print("🔁 Relaunching main.py to listen for wake word...")
                subprocess.Popen(["python3", "main.py"])
            except FileNotFoundError:
                print("❌ Could not find main.py.")

        else:
            print(f"❓ Unknown toggle action: {toggle_action}")
    else:
        print(f"❓ Unknown intent: {intent}")

def main():
    try:
        with open("./.temp/intent_and_slots.json", "r") as f:
            data = json.load(f)
            intent = data.get("intent")
            slots = data.get("slots", {})
        
        execute_command(intent, slots)

    except FileNotFoundError:
        print("❌ intent_and_slots.json not found.")
    except json.JSONDecodeError:
        print("❌ Could not decode intent_and_slots.json.")

if __name__ == "__main__":
    main()
