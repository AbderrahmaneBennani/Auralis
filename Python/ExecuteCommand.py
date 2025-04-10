import json

def execute_command(intent, slots):
    if intent == "play":
        print("🎶 Playing music...")
        # Add your code to play music here, using slots if needed
        if "song" in slots:
            print(f"🎵 Playing song: {slots['song']}")
    elif intent == "stop":
        print("⏹️ Stopping music...")
        # Add your code to stop music here
    else:
        print(f"❓ Unknown intent: {intent}")

def main():
    # Read the intent and slots from the JSON file
    try:
        with open("intent_and_slots.json", "r") as f:
            data = json.load(f)
            intent = data["intent"]
            slots = data["slots"]
        
        # Execute the command based on the intent and slots
        execute_command(intent, slots)
    except FileNotFoundError:
        print("❌ intent_and_slots.json not found. Make sure the previous script has run.")
    except json.JSONDecodeError:
        print("❌ Error decoding the intent and slots data.")
    
if __name__ == "__main__":
    main()
