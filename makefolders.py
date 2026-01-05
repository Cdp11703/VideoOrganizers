import os
import shutil

# Set the path to your anime folder
base_path = os.getcwd()

# List all video files (assuming .mp4, .mkv, .avi, etc.)
video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv')
video_files = [f for f in os.listdir(base_path) if f.lower().endswith(video_extensions)]

# Path to the .nomedia file (create if not exists)
nomedia_path = os.path.join(base_path, ".nomedia")
if not os.path.exists(nomedia_path):
    open(nomedia_path, 'a').close()

for video in video_files:
    # Remove extension for folder name
    folder_name = os.path.splitext(video)[0]    
    
    # Parse the folder name to extract episode number
    anything, epnum = folder_name.split("_-_", 1)
    episode_number, resolution, subtitler = epnum.split("_", 2)
    folder_name = f"Episode {episode_number.lstrip('0')}"

    print(folder_name)
    folder_path = os.path.join(base_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # Copy .nomedia into the new folder
    shutil.copy2(nomedia_path, folder_path)

    # Move the video file into the new folder
    shutil.move(os.path.join(base_path, video), os.path.join(folder_path, video))  
    print(f"Moved {video} to {folder_path}")
    