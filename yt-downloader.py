import yt_dlp
import shutil
import sys
import os

def banner():
    banner = r"""
----------------------------------------------------------


                    by Diogo S. Lourenço


----------------------------------------------------------
      """
    print(f"\n\n{banner}\n\n")
    
def verify_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("[X] FFmpeg is not installed or not added to PATH.\n")
        print("Follow the steps below to resolve it on Windows:")
        print("1. Download FFmpeg here: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
        print("2. Extract the contents of the ZIP.")
        print("3. Go to the 'bin' folder and copy the path (e.g., C:\\ffmpeg\\bin)")
        print("4. Add this path to the system environment variables (variable 'Path')")
        print("5. Close and reopen the terminal.")
        print("6. Test in the terminal with: ffmpeg -version\n")
        sys.exit(1)

def get_titles(wordlist_path):
    with open(wordlist_path, 'r') as f:
        urls = [url.strip() for url in f if url.strip()]

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    titles = []
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                info = ydl.extract_info(url, download=False)
                titles.append(info.get('title', 'Title not found'))
            except:
                titles.append(None)
    return titles

def download_videos(wordlist_path, format='mp3'):
    if format == 'mp3':
        os.makedirs("mp3", exist_ok=True)

        verify_ffmpeg()
        yt_opts = {
            'quiet': True,
            'no_warnings': True,
            'outtmpl': os.path.join('mp3', '%(title)s.%(ext)s'),
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        os.makedirs("video", exist_ok=True)
        
        yt_opts = {
            'quiet': True,
            'no_warnings': True,
            'outtmpl': os.path.join('video', '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
        }

    titles = get_titles(wordlist_path)

    with open(wordlist_path, 'r') as f:
        urls = [url.strip() for url in f if url.strip()]

    failed = []
    success_count = 0

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        for url, title in zip(urls, titles):
            if title:
                print(f"[+] Downloading ({format.upper()}): {title}")
            else:
                print(f"[+] Downloading ({format.upper()}): {url} (Title not found)")

            try:
                ydl.download([url])
                print("[✓] Download completed.\n")
                success_count += 1
            except yt_dlp.utils.PostProcessingError as e:
                if "Permission denied" in str(e):
                    print(f"\n[X] {url}: Possible file open or you don't have permission to save the file.\n")
                else:
                    print(f"\n[X] Post-processing error: {e}\n")
                failed.append(url)
            except Exception as e:
                print(f"\n[X] Error downloading {url}: {e}\n")
                failed.append(url)

    # Result summary
    total = len(urls)
    print(f"\n[!] Download Summary: {success_count}/{total} downloads completed successfully.\n")

    if failed:
        print("[!] Links that failed to download:\n")
        for link in failed:
            print(link)
        input("\nPress ENTER to close...")
    else:
        input("\nPress ENTER to close...")

if __name__ == '__main__':
    banner()
    wordlist_path = input("File .txt with links (e.g., links.txt):\n$ ").strip()

    print("\nChoose download format:\n")
    print("[1] MP3 (audio only)")
    print("[2] MP4 (full video)")

    choice = input("\nOption: ").strip()
    print("\n[*] Loading links...\n")

    if choice == '1':
        format = 'mp3'
    elif choice == '2':
        format = 'mp4'
    else:
        print("[X] Invalid option. Use only 1 or 2.")
        sys.exit(1)

    download_videos(wordlist_path, format)

