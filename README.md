# VideoOrganizers
This repository contains a collection of small Python utility scripts used for organizing, managing, and playing local video (anime) files. The scripts automate common tasks such as generating playlists, organizing episodes into folders, playing videos via mpv, and flattening directory structures by moving video files.

# File Descriptions
create_list.py

Scans a directory for video files and generates a text-based playlist (.txt) containing all detected videos, sorted alphabetically.

makefolders.py

Automatically organizes video files into episode-based folders by parsing filenames, creates per-episode directories, adds a .nomedia file, and moves each video into its corresponding folder.

play_list.py

Plays a previously generated playlist file using the mpv media player by launching it from the terminal.

removevideo.py

Flattens a directory structure by moving .mp4 files out of subfolders back into the main directory.

# Notes
Designed for local media organization, particularly anime episode collections.

Some scripts assume specific filename formats (e.g., episode number parsing).

mpv must be installed and available in the system PATH for playlist playback.
