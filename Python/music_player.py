# music_player.py - Create this as a standalone script
import pygame
import sys
import os
import time
import signal

# File to store the PID of the music process
PID_FILE = "/tmp/music_player.pid"

def write_pid():
    """Write the current process ID to a file"""
    with open(PID_FILE, 'w') as f:
        f.write(str(os.getpid()))

def cleanup():
    """Remove the PID file when exiting"""
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)

def play():
    """Start playing music"""
    # Setup signal handler for clean exit
    signal.signal(signal.SIGTERM, lambda signum, frame: sys.exit(0))
    
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()
    
    # Write PID to file for easy identification
    write_pid()
    
    try:
        # Register cleanup on exit
        atexit.register(cleanup)
        
        # Play music
        music_file = "../Media/music.wav"
        if not os.path.exists(music_file):
            print(f"Error: Music file not found at {os.path.abspath(music_file)}")
            sys.exit(1)
            
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        
        print(f"Music playing with PID {os.getpid()}")
        
        # Keep playing until interrupted
        while pygame.mixer.music.get_busy():
            time.sleep(1)
            
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cleanup()
        pygame.quit()

if __name__ == "__main__":
    import atexit
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "stop":
            # Stop the music if running
            if os.path.exists(PID_FILE):
                try:
                    with open(PID_FILE, 'r') as f:
                        pid = int(f.read().strip())
                    
                    # Try to kill the process
                    os.kill(pid, signal.SIGTERM)
                    print(f"Stopped music process with PID {pid}")
                    
                    # Remove PID file in case the process doesn't
                    if os.path.exists(PID_FILE):
                        os.remove(PID_FILE)
                except ProcessLookupError:
                    print("Music process not found. It may have already been stopped.")
                    if os.path.exists(PID_FILE):
                        os.remove(PID_FILE)
                except Exception as e:
                    print(f"Error stopping music: {e}")
            else:
                print("No music process found to stop.")
        else:
            print(f"Unknown command: {command}")
            print("Usage: python music_player.py [play|stop]")
    else:
        # Default action is to play
        play()