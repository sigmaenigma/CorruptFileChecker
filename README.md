# Corrupt File Checker

## Overview
This Python script scans a specified directory for video files and checks for corruption using Docker and FFMPEG. It logs the results in a file called `corruption_log.txt`, indicating whether each file is corrupted or not.

## Requirements
- **Docker** must be installed and running on your system.
- The **linuxserver/ffmpeg** Docker image is used for processing.
- **Python 3.x** must be installed.

## Supported Formats
The script checks video files with the following extensions:
- MP4 (`.mp4`)
- MKV (`.mkv`)
- AVI (`.avi`)
- MOV (`.mov`)
- FLV (`.flv`)

## Usage

1. **Clone or download the script**
2. **Modify the directory path**
   
   Update the `DIR` variable to point to the folder containing your video files:
   ```python
   DIR = "/path/to/folder"
   ```
3. **Run the script**
   Execute the script using Python:
   ```sh
   python3 script.py
   ```
   
4. **Check the log file**
   After execution, review `corruption_log.txt` for the results:
   ```sh
   cat corruption_log.txt
   ```

## How It Works
- The script scans the specified directory recursively for video files.
- It uses Docker to run an FFMPEG container and process each file.
- If corruption is detected, the filename is logged in `corruption_log.txt`.
- If no corruption is found, the file is marked as clean in the log.

## Example Output
```
Corruption detected in: /path/to/folder/video1.mkv
No corruption detected in: /path/to/folder/video2.mp4
```

## Troubleshooting
- **Docker not found:** Ensure Docker is installed and running.
- **Permission issues:** Try running with `sudo` if necessary.
- **Missing files in log:** Confirm the directory path and supported formats.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
