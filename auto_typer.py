import sys
import pyautogui
import time

MILLISECONDS_TO_SLEEP = 100
# Number of milliseconds to sleep after typing each letter
# Minimum 100 recommended
SAFETY = 0.25
# Safe zone at upper left corner of the screen
DEBUG = True
# To show logs on the console


pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

if len(sys.argv) != 2:
    print("Usage: auto_typer.py file_name")
    exit(-1)

file_name = sys.argv[1]
with(open(file_name, 'rt')) as f:
    content = f.read()

Width, Height = pyautogui.size()
time.sleep(1)
pause_zone = False
if DEBUG:
    print("Starting to type...")
index = 0
while index<len(content):
    letter = content[index]
    time.sleep(MILLISECONDS_TO_SLEEP / 1000)
    x, y = pyautogui.position()
    safe = x>Width*SAFETY and y>Height*SAFETY
    if safe:
        pause_zone = False
        pyautogui.typewrite(letter)
        index += 1
        if DEBUG:
            print(letter, end='')
    else:
        if DEBUG:
            if not pause_zone:
                pause_zone = True
                print("\n<Cursor in safe zone>")
