import os
import subprocess

def create_list(directory=".", playlist_filename="my_list.txt"):
    """
    Creates a playlist file from video files in a specified directory
    and then plays it using mpv in a terminal.

    Args:
        directory (str): The directory to scan for video files. Defaults to the current directory.
        playlist_filename (str): The name of the playlist file to create.
    """
    # Define common video file extensions
    video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm')

    playlist_path = os.path.join(directory, playlist_filename)
    video_files = []

    # Get list of video files in the specified directory
    try:
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)) and item.lower().endswith(video_extensions):
                video_files.append(item)
        video_files.sort() # Optional: Sort the files alphabetically
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        return
    except Exception as e:
        print(f"An error occurred while listing directory contents: {e}")
        return

    if not video_files:
        print(f"No video files found in '{directory}'. No playlist created.")
        return

    # Write video file names to the playlist file
    try:
        with open(playlist_path, 'w') as f:
            for video in video_files:
                f.write(video + '\n')
        print(f"Playlist '{playlist_filename}' created successfully in '{directory}'.")
    except IOError as e:
        print(f"Error writing to playlist file: {e}")
        return

if __name__ == "__main__":
    # --- Configuration ---
    # Set the directory where your video files are located.
    # If your .py script is in the same folder as your videos, use "."
    # Otherwise, specify the full path, e.g., r"C:\Users\YourUser\Videos" or "/home/youruser/videos"
    target_directory = "."
    playlist_name = "my_list.txt"
    # ---------------------

    create_list(target_directory, playlist_name)