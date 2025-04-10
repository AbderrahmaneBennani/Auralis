import subprocess

def listen_for_keyword(keyword="or alice"):
    cmd = [
        "../Whisper/Scripts/whisper-stream",
        "-m", "../Whisper/Models/ggml-tiny.en.bin",
        "-t", "8",
        "--step", "500",
        "--length", "5000"
    ]

    try:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        print(f"Listening for keyword: '{keyword}'...")

        for line in process.stdout:
            line = line.strip()
            if line:
                print(f"> {line}")  # Optional: Show live transcript
                if keyword.lower() in line.lower():
                    print("Successful")
                    process.terminate()
                    break

    except KeyboardInterrupt:
        print("Stopped by user.")
        process.terminate()

if __name__ == "__main__":
    listen_for_keyword("Or Alice")
