import os
import subprocess
import sys

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
    if len(sys.argv) < 3:
        print("Usage: python3 app.py <single|multi> <file|folder path>")
        sys.exit(1)

    mode = sys.argv[1]
    path = sys.argv[2]

    with open(LOGFILE, "w") as log_file:
        log_file.write("")

    if mode == "single":
        if os.path.isfile(path) and any(path.endswith(f".{fmt}") for fmt in FORMATS):
            print(f"Checking: {path}")
            check_corruption(path)
        else:
            print("Invalid file or unsupported format.")
            sys.exit(1)

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
            sys.exit(1)

    else:
        print("Invalid mode. Use 'single' or 'multi'.")
        sys.exit(1)

    print(f"Corruption check completed. Results are logged in {LOGFILE}.")

if __name__ == "__main__":
    main()
