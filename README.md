<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0d0221,240046,3c096c,5a189a,7209b7&height=180&section=header&text=yt-downloader&fontColor=ffffff&fontSize=40&animation=fadeIn" />
</p>

# 🎬 **DamLoader** - YouTube Video Downloader 🔥

This simple project is a Python script designed to make your video/audio downloading from YouTube a breeze.  
With a list of URLs, you can easily grab the content you need, either as an MP3 audio or full MP4 video.  
Developed with **Python** and powered by **yt-dlp**, it’s fast, efficient, and ready to rock!

---

## ⚙️ **Requirements** 🛠️

Before running the script, make sure you have these tools installed:

- **Python 3.x** (3.6+ recommended)  
- **FFmpeg** (required for MP3 downloads)

### Install Dependencies with `pip`

Run this to install the necessary libraries:

```bash
pip install -r requirements.txt
```

### Installing FFmpeg

If you need MP3 downloads, make sure FFmpeg is installed:

1. Download FFmpeg from [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).
2. Extract the ZIP.
3. Copy the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).
4. Add the path to your **system’s environment variables** (`Path`).
5. Restart your terminal.
6. Check the installation with: `ffmpeg -version`.

---

## 🏃 **Usage (For Python Script)** 🚀

1. **Download** the `yt-downloader.py` script.
2. Prepare a `.txt` file with YouTube URLs (one URL per line).
3. Run the script via terminal:

```bash
python yt-downloader.py
```

4. The script will prompt you for the URL file path.
5. Choose your download format:
   - `1` for MP3 (audio)
   - `2` for MP4 (full video)

The script will handle the download!

---

## ⚠️ **Troubleshooting** 🛠️

- **FFmpeg not found**: Follow the instructions above to install FFmpeg.
- **Permission Denied**: Ensure no other app is using the file and that you have write permissions.
- **Other Errors**: Verify URLs, check for internet access, and ensure proper script setup.

---

## 🖤 **License** 💡

Idk what is this :D

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0d0221,240046,3c096c,5a189a,7209b7&height=100&section=footer" />
</p>
