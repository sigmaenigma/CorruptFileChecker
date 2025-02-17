# Video Corruption Check

## Description
This script checks for corruption in video files using `ffmpeg` inside a Docker container. It supports scanning either a single file or an entire folder containing multiple video files. The results are logged in `corruption_log.txt`.

## Prerequisites
- Python 3
- Docker
- `ffmpeg` (via `linuxserver/ffmpeg` Docker image)

## Supported Formats
- MP4
- MKV
- AVI
- MOV
- FLV

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/sigmaenigma/CorruptFileChecker.git
   cd CorruptFileChecker
   ```
2. Ensure Docker is installed and running.

## Usage
Run the script with either `single` or `multi` mode:

- To check a single video file:
  ```sh
  python3 app.py single /path/to/video.mp4
  ```
- To scan an entire folder:
  ```sh
  python3 app.py multi /path/to/folder
  ```

## Output
The script logs the results in `corruption_log.txt`, indicating whether corruption was detected in each file.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

