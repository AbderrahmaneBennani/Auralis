import json
import subprocess
import os
import paho.mqtt.client as mqtt

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

        elif toggle_action == "stop":
            print("⏹️ Stopping music...")

            # Kill all aplay processes (or replace with smarter PID tracking)
            subprocess.call(["pkill", "-f", "aplay"])
            print("✅ Music stopped.")
    
    elif intent == "changeLightState":
        # MQTT Configuration
        MQTT_BROKER = "localhost"  # Your MQTT broker address
        MQTT_PORT = 1883  # MQTT port (default is 1883)
        MQTT_TOPIC = "zigbee2mqtt/Bulb1/set"  # Topic for your lightbulb

        # Initialize MQTT client
        client = mqtt.Client()
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        toggle_action = slots.get("state")

        if toggle_action == "on":
            print("Turning lights on...")
            try:
                # Publish MQTT message to turn on the light
                client.publish(MQTT_TOPIC, '{"state": "ON"}')
                print("✅ Light turned on.")
            except Exception as e:
                print(f"❌ Error turning on light: {e}")

        elif toggle_action == "off":
            print("Turning lights off...")
            try:
                # Publish MQTT message to turn off the light
                client.publish(MQTT_TOPIC, '{"state": "OFF"}')
                print("✅ Light turned off.")
            except Exception as e:
                print(f"❌ Error turning off light: {e}")
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
