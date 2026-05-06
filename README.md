# Auto Extraction Music Script

- Developed a Python-based music extraction pipeline to batch download and organize audio from YouTube playlists, reducing manual processing for large music libraries.
- Integrated yt-dlp and FFmpeg to extract high-quality audio, convert files into MP3 format, and save outputs automatically into a structured local folder.
- Implemented playlist-based batch processing with error handling, download throttling, Windows-safe filenames, and automated file naming using playlist order and video titles.
- Improved the original UI automation workflow by replacing manual browser clicking, screenshot capture, and converter-site interactions with a more reliable script-based download process.

# QnA:
1. Why did I build it?
Simply put, I have at least 250 songs saved in my YouTube playlist, and I needed a way to download all of them as MP3 files for my phone.

2. Why not just use an existing music downloader?
I could have, but I had two reasons. First, I wanted to practice automation, scripting, and Python. 

3. Why used yt-dlp and FFmpeg?

- Long story short, after downloading all the music, I needed to rename the metadata for each file. However, I realized that editing metadata can be fragile, and some music files became partially corrupted. My next idea was to re-convert the music files to fix the corrupted parts. This worked for a few songs at a time, so I thought, why not convert everything at once?
- Unfortunately, that corrupted the entire batch. All of the music files became 0 KB, which basically meant the files were gone. I also had no backup. At that point, I had no choice but to download the music again, which I expected to take the whole day.
- After going down a rabbit hole of searching for a better solution, I found two open-source tools: yt-dlp and FFmpeg. yt-dlp is a YouTube downloader that can download videos or playlists, but the audio is often downloaded in formats like WebM. FFmpeg handles the conversion from WebM or other audio formats into MP3.
- The biggest benefit was that yt-dlp could download the entire playlist automatically. After running it, the full playlist took about 30 minutes to download and convert. My original approach would have taken around 3 days, so this reduced the total time by about 90%.
- Link for yt-dlp: https://github.com/yt-dlp/yt-dlp
- Link for FFmpeg: https://github.com/ffmpeg/ffmpeg

4. Would I improve this if given feedback?
Yes, absolutely. If I have the time and opportunity. This is a passion project and a practical solution for managing my music library.

~~3. Why use coordinates?
Currently, I am using a library that controls mouse and keyboard actions based on screen coordinates. In the future, I plan to explore more robust approaches, such as using image recognition or screenshot matching to make the automation less dependent on fixed positions.~~

~~Second, I wanted full control over the process—automatically grabbing links, downloading music, and using an AI chatbot to generate clean file names. I also needed control over execution timing, since some websites take longer to load.~~
