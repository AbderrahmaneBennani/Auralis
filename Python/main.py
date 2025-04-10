import subprocess

def run_script(script_name):
    print(f"\n🔄 Starting {script_name}...")
    try:
        result = subprocess.run(["python3", script_name], check=True)
        print(f"✅ {script_name} finished successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ {script_name} failed with exit code {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"❌ Could not find {script_name}. Make sure it exists.")
        return False
    return True

if __name__ == "__main__":
    scripts_in_order = [
        "ListenWakeWord.py",
        "SpeechToIntent.py",
        "ExecuteCommand.py"
    ]

    for script in scripts_in_order:
        success = run_script(script)
        if not success:
            print("🚫 Stopping due to error.")
            break
