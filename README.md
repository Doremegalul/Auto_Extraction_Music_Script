# Auto Extraction Music Script

- Developed a Python automation script to streamline downloading and organizing music by integrating browser control, clipboard handling, and UI automation.
- Automated multi-step workflows including URL extraction, conversion, screenshot capture, and file renaming using PyAutoGUI and Pyperclip.
- Implemented coordinate-based interaction and loop execution to batch process multiple songs efficiently, reducing manual effort.

# QnA:
1. Why did I build it?
Simply put, I have at least 250 songs saved in my YouTube playlist, and I needed a way to download all of them as MP3 files for my phone.

2. Why not just use an existing music downloader?
I could have, but I had two reasons. First, I wanted to practice automation, scripting, and Python. Second, I wanted full control over the process—automatically grabbing links, downloading music, and using an AI chatbot to generate clean file names. I also needed control over execution timing, since some websites take longer to load.

3. Why use coordinates?
Currently, I am using a library that controls mouse and keyboard actions based on screen coordinates. In the future, I plan to explore more robust approaches, such as using image recognition or screenshot matching to make the automation less dependent on fixed positions.

4. Would I improve this if given feedback?
Yes, absolutely—if I have the time and opportunity. This is a passion project and a practical solution for managing my music library.
