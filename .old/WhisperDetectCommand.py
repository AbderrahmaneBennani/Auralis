import subprocess

def run_command():
    # Define the command to run
    command = [
        '../Whisper/Scripts/whisper-command',
        '-m', '../Whisper/Models/ggml-tiny.en.bin',
        '-cmd', '../Whisper/Commands/commands.txt',
        '-ac', '128',
        '-t', '3',
        '-c', '0'
    ]

    # Start the subprocess and capture both stdout and stderr
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True
    )

    # Read the output and print it in real-time
    try:
        for stdout_line in process.stdout:
            print(stdout_line.strip())  # Print each line from stdout

        for stderr_line in process.stderr:
            print(f"STDERR: {stderr_line.strip()}")  # Print any error from stderr

    except Exception as e:
        print(f"Error: {e}")
    finally:
        process.wait()  # Ensure the process finishes

if __name__ == "__main__":
    run_command()
