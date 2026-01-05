# File Descriptions
- ```create_list.py``` scans a directory for video files and generates a text-based playlist (.txt) containing all detected videos, sorted alphabetically.
- ```makefolders.py``` organizes video files into episode-based folders by parsing filenames, creates per-episode directories, adds a .nomedia file, and moves each video into its corresponding folder.
- ```play_list.py``` plays a previously generated playlist file using the mpv media player by launching it from the terminal.
- ```removevideo.py``` flattens a directory structure by moving .mp4 files out of subfolders back into the main directory.

# Notes
- Designed for local media organization, particularly video collections.
- Some scripts assume specific filename formats. The user may change the code (e.g., number parsing).
- Some video players like mpv must be installed and available in the system PATH for playlist playback.
