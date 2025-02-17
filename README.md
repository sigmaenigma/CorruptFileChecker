# Corrupt File Checker

This project uses Docker and ffmpeg to check video files for corruption. The script supports both single-file and multi-file modes, allowing you to scan individual videos or entire directories.

## Prerequisites

- Python 3.x
- Docker
- ffmpeg

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sigmaenigma/CorruptFileChecker.git
    ```
2. Navigate to the project directory:
    ```bash
    cd video-corruption-checker
    ```
3. Install any required Python packages (if applicable).

## Usage

### Single File Mode

To check a single video file for corruption, run the following command:

```bash
python3 app.py -m single -f /path/to/video.mp4
```

### Multi File Mode

To check all video files in a directory for corruption, run the following command:

```bash
python3 app.py -m multi -f /path/to/folder
```

## Arguments

- `-m`, `--mode`: Mode of operation (`single` or `multi`).
- `-f`, `--file`: Path to the video file or directory.

## Log Output

The script generates a log file named `corruption_log.txt` in the project directory. This file contains the results of the corruption checks, indicating whether each file is corrupted or not.

## Example

To check a single video file:
```bash
python3 app.py -m single -f /home/user/videos/movie.mp4
```

To check all video files in a directory:
```bash
python3 app.py -m multi -f /home/user/videos
```

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions to improve the script are welcome!

## License

This project is licensed under the MIT License.
