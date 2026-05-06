import yt_dlp # pip install yt-dlp 
from pathlib import Path # winget install Gyan.FFmpeg

OUTPUT_FOLDER = Path(r"INSERT YOUR FILE PATH WAY HERE")

PLAYLIST_URL = "INSERT YOUR PLAYLIST LINK HERE. MAKE SURE IT IS PUBLIC OR UNLISTED"


def download_playlist_as_mp3(playlist_url):
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        # Best available audio from YouTube
        "format": "bestaudio/best",

        # Save location and filename format
        "outtmpl": str(OUTPUT_FOLDER / "%(playlist_index)s - %(title)s.%(ext)s"),

        # Continue even if one video fails
        "ignoreerrors": True,

        # Slow down a bit to reduce errors
        "sleep_interval": 3,
        "max_sleep_interval": 8,

        # Convert to MP3 using FFmpeg
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],

        # Safer Windows filenames
        "windowsfilenames": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if __name__ == "__main__":
    download_playlist_as_mp3(PLAYLIST_URL)