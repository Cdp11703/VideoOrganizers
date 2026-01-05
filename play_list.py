import os
import subprocess

def play_playlist(directory=".", playlist_filename="my_list.txt"):
    # Run mpv with the playlist
    try:
        # We need to change the current working directory for the subprocess
        # so mpv can find the video files relative to the playlist.
        print(f"Attempting to play videos using mpv --playlist={playlist_filename}...")
        subprocess.run(['mpv', f'--playlist={playlist_filename}'], cwd=directory)
    except FileNotFoundError:
        print("Error: 'mpv' command not found. Please ensure mpv is installed and in your system's PATH.")
    except Exception as e:
        print(f"An error occurred while trying to run mpv: {e}")

if __name__ == "__main__":
    # --- Configuration ---
    # Set the directory where your video files are located.
    # If your .py script is in the same folder as your videos, use "."
    # Otherwise, specify the full path, e.g., r"C:\Users\YourUser\Videos" or "/home/youruser/videos"
    target_directory = "."
    playlist_name = "my_list.txt"
    # ---------------------

    play_playlist(target_directory, playlist_name)