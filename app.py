import os
import subprocess
import argparse

# Log file
LOGFILE = "corruption_log.txt"

# Supported movie formats
FORMATS = ["mp4", "mkv", "avi", "mov", "flv"]

# Function to check for corruption using Docker
def check_corruption(file):
    try:
        print(f'Creating and running Docker image...')
        result = subprocess.run(
            [
                "docker", "run", "--rm", "-v",
                f"{os.path.abspath(os.path.dirname(file))}:/videos",
                "linuxserver/ffmpeg:latest",
                "-v", "error", "-i", f"/videos/{os.path.basename(file)}", "-f", "null", "-"
            ],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        with open(LOGFILE, "a") as log_file:
            if result.returncode != 0:
                log_file.write(f"Corruption detected in: {file}\n")
            else:
                log_file.write(f"No corruption detected in: {file}\n")
        return True
    except Exception as e:
        print(f'An issue occured running check_corruption(): {e}')
        return False

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Check video files for corruption using Docker and ffmpeg.')
    parser.add_argument('-m', '--mode', choices=['single', 'multi'], required=True, help='Mode of operation: single file or multiple files in a directory')
    parser.add_argument('-f', '--file', required=True, help='Path to the video file or directory')

    # Parse arguments
    args = parser.parse_args()

    mode = args.mode
    path = args.file

    with open(LOGFILE, "w") as log_file:
        log_file.write("")

    if mode == "single":
        if os.path.isfile(path) and any(path.endswith(f".{fmt}") for fmt in FORMATS):
            print(f"Checking: {path}")
            check_corruption(path)
        else:
            print("Invalid file or unsupported format.")
    elif mode == "multi":
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if any(file.endswith(f".{fmt}") for fmt in FORMATS):
                        file_path = os.path.join(root, file)
                        print(f"Checking: {file_path}")
                        check_corruption(file_path)
        else:
            print("Invalid directory.")
    else:
        print("Invalid mode. Use 'single' or 'multi'.")

    print(f"Corruption check completed. Results are logged in {LOGFILE}.")

if __name__ == "__main__":
    main()
