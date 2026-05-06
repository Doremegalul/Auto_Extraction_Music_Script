import pyautogui as pg
import time
import pyperclip

pg.FAILSAFE = True
pg.PAUSE = 0.2


def mouse_coordinate():
    time.sleep(3)
    x, y = pg.position()
    print(str(x) + ", " + str(y))
    return x, y


def mouse_click(x, y):
    time.sleep(1)
    pg.click(x, y)


def copy_clean_youtube_url():
    pg.hotkey("ctrl", "l")   # Select URL bar
    time.sleep(0.3)
    pg.hotkey("ctrl", "c")   # Copy URL
    time.sleep(0.3)

    url = pyperclip.paste()

    # Remove playlist/tracking parts
    url = url.split("&list=")[0]
    url = url.split("&index=")[0]
    url = url.split("&pp=")[0]

    pyperclip.copy(url)
    print("Copied clean URL:", url)


def run_automation():
    print("Starting in 5 seconds. Switch to YouTube now.")
    time.sleep(5)

    # =====================
    # YouTube: copy clean link from URL bar
    # =====================
    copy_clean_youtube_url()

    # =====================
    # MP3 Converter: paste link and convert
    # =====================
    mouse_click(398, 15)    # MP3 Converter tab
    mouse_click(756, 584)   # Search/input box
    pg.hotkey("ctrl", "v")  # Paste clean YouTube link

    mouse_click(1044, 583)  # Bitrate dropdown
    mouse_click(1038, 809)  # Bitrate selection kb/s
    mouse_click(1300, 586)  # Convert

    time.sleep(15)
    mouse_click(1108, 588)  # Convert again/download

    # =====================
    # YouTube: screenshot title area
    # =====================
    mouse_click(206, 17)  # YouTube tab

    pg.hotkey("winleft", "shift", "s")  # Windows screenshot tool
    time.sleep(1)

    pg.moveTo(87, 550)  # Screenshot start
    pg.dragTo(1389, 1001, duration = 0.4, button = "left")  # Screenshot end

    # =====================
    # ChatGPT: paste screenshot and send
    # =====================
    mouse_click(344, 1055)  # Chrome icon
    mouse_click(935, 973)   # ChatGPT text box

    pg.hotkey("ctrl", "v")  # Paste screenshot

    time.sleep(2)
    mouse_click(1446, 979)  # Send prompt

    mouse_click(696, 377)
    time.sleep(8)
    pg.dragTo(1480, 372, duration = 2, button = "left")
    pg.hotkey("ctrl", "c")  # Copy title/result

    # =====================
    # Folder: sort newest file and rename
    # =====================
    mouse_click(212, 1061)  # Folder icon
    mouse_click(523, 141)   # Date modified
    mouse_click(523, 141)   # Date modified again

    time.sleep(2)           # Modify depending on music length
    mouse_click(485, 198)
    pg.rightClick(485, 198) # Right click newest file

    time.sleep(2)
    mouse_click(587, 826)   # Rename option
    time.sleep(0.5)
    pg.hotkey("ctrl", "v")  # Paste copied title

    # =====================
    # Firefox / YouTube: next video
    # =====================
    mouse_click(298, 1059)   # Firefox icon
    mouse_click(1162, 364)   # Close share popup / X if needed
    pg.hotkey("shift", "n")  # Move to next video

def loop_manual():
    count = int(input("How many songs to process? "))

    for i in range(count):
        print(f"Running song {i+1}/{count}")

        try:
            run_automation()
            time.sleep(2)
        except Exception as e:
            print("Error:", e)
            break

def loop_manual_temporary_rename ():
    count = int(input("How many songs to process? "))

    for i in range(count):
        print(f"Running song {i+1}/{count}")

        try:
            temporary_rename()
            time.sleep(2)
        except Exception as e:
            print("Error:", e)
            break

def temporary_rename():
    # This is for rename the VLC file itself. Not the mp3 file. You need to change the meta data.
    
    print("Starting in 1 seconds. Switch to the folder now.")
    time.sleep(1)

    pg.rightClick(325, 201) # Right click the file
    mouse_click(442, 819) # Click rename
    pg.hotkey("ctrl", "c")  # Copy name
    mouse_click(1396, 197) # Exit out of the name

    pg.rightClick(325, 201) # Right click the file again
    mouse_click(335, 221) # Click play
    time.sleep(0.5)
    #mouse_click(646, 1058) # Click the bottom app

    pg.rightClick(241, 107) # Right click the file in vlc
    mouse_click(312, 190) # Click information

    mouse_click(733, 374) # Click the title
    pg.hotkey("ctrl", "a") # Highlight the title
    pg.hotkey("ctrl", "v") # Paste the new title

    mouse_click(1156, 769) # Save Metadata
    mouse_click(1250, 767) # Close

    mouse_click(1890, 10) # X it out



if __name__ == "__main__":
    #mouse_coordinate()  # Turn on to get coordinate, turn off once finished

    # NOTE: Remember to have YouTube, MP3 Convertor, AI Assistance, and Folder ready.
    #loop_manual()

    loop_manual_temporary_rename()
