# DamLoader - YouTube Video Downloader

**DamLoader** is a Python script that allows you to download videos or audio from YouTube using a list of URLs. You can choose to download either the audio in MP3 format or the full video in MP4 format.

---

## Requirements

Before running the script, make sure you have the following requirements installed:

1. **Python 3.x** (Python 3.6 or above)
2. **FFmpeg** (For MP3 download)
   - FFmpeg is required to convert the audio to MP3 format. Please follow the instructions below to install FFmpeg on Windows.
   
3. **Python Libraries**:
   - `yt-dlp`: A powerful tool to download videos from YouTube.
   - `pyfiglet`: To create ASCII art for the banner.

### Installing Requirements:

#### Install Python libraries:
Run the following command to install the required libraries via `pip`:

```bash
pip install -r requirements.txt
```

#### Install FFmpeg:
1. Download FFmpeg here: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2. Extract the contents of the ZIP file.
3. Go to the `bin` folder and copy the path (e.g., `C:\\ffmpeg\\bin`).
4. Add this path to the system environment variables (variable `Path`).
5. Close and reopen your terminal.
6. Test FFmpeg installation with: `ffmpeg -version`.

---

## Usage (For Python Script)

1. Download the `DamLoader.py` script to your computer.
2. Prepare a text file containing a list of YouTube URLs (one URL per line).
3. Run the script:

```bash
python DamLoader.py
```

4. The script will ask for the path to the text file with URLs. Enter the file path when prompted.
5. Choose the download format:
   - `1` for MP3 (audio only)
   - `2` for MP4 (full video)

The script will download the content based on your choice.

---

## Usage (For Executable .exe)

If you don't have Python installed, you can use the executable file (`DamLoader.exe`) instead.

1. Download the `DamLoader.exe` file from the releases section of this repository.
2. Prepare a text file containing a list of YouTube URLs (one URL per line).
3. Run the executable by double-clicking on it.
4. The program will ask for the path to the text file with URLs. Enter the file path when prompted.
5. Choose the download format:
   - `1` for MP3 (audio only)
   - `2` for MP4 (full video)

The `.exe` file will perform the download based on your selection.

---

## Troubleshooting

- **FFmpeg not found**: If you see an error that FFmpeg is not installed or not in the system's `PATH`, follow the installation instructions above to install FFmpeg.
- **Permission Denied**: If you encounter a "Permission denied" error, make sure no other program is using the file you're trying to save or ensure you have the necessary permissions to write to the folder.
- **Other errors**: Please check the error message and make sure that the URLs are correct and accessible.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# Steps to use `.exe`

- **For those who do not have Python installed**:
- Go to the releases section of the GitHub repository and download `DamLoader.exe`.
- Prepare a text file with a list of YouTube URLs (one URL per line).
- Double-click the `DamLoader.exe` file to run it.
- The program will ask for the path to the text file with the links. Enter the path when prompted.
- Choose the download format:
- `1` for MP3 (audio only)
- `2` for MP4 (full video)

- **For those who have Python installed**:
- Download the `DamLoader.py` script to your computer.
- Prepare a text file with the YouTube links. - Run the script with the command:

```bash
python DamLoader.py
```

- The script will ask for the path to the text file with the links. Enter the path when prompted.
- Choose the download format as described above.

---
### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
