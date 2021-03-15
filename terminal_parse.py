import pyautogui
import pyperclip
import os
import re
import time as t
from pygame import mixer  # Load the popular external library


DIRECTORY = '/Users/alexanderhaislip/Projects/Terminal_Jeopardy'
TEXT_FILE = '---TERMINAL_CAPTURE---.TXT'
MUSIC = 'Jeopardy_Theme Song.mp3'
MP3_PATH = DIRECTORY + '/' + MUSIC
FOUND = True

# send 'command A' and copy all text
# paste clipboard to a file in the background
# delete file contents after a certain amount of time
def fetch_terminal():
    pyautogui.keyDown('command')
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    pyautogui.keyUp('command')

    pyautogui.keyDown('command')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('command')

    os.getcwd()
    os.chdir(DIRECTORY)
    # pasting the text from clipboard
    s = pyperclip.paste()
    with open(TEXT_FILE, 'w') as g:
        g.write(s)
        return


def look_for_install():
    term = 'install'

    with open(DIRECTORY + '/' + TEXT_FILE) as f:
        if 'install' in f.read():
            print("found " + term)
            print("Playing Jeopardy theme song...")
            mixer.init()
            # needs to be a universal path vvv
            mixer.music.load('/Users/alexanderhaislip/Projects/Terminal_Jeopardy/Jeopardy_Theme Song.mp3')
            mixer.music.play()
            t.sleep(15)
            print("Playing...")
            fileVariable = open(DIRECTORY + '/' + TEXT_FILE, 'r+')
            fileVariable.truncate(0)
            fileVariable.close()
            return


def look_for_done():
    term = 'done'

    with open(DIRECTORY + '/' + TEXT_FILE) as f:
        if 'done' in f.read():
            print("found " + term)
            print("Stopping Jeopardy theme song...")
            mixer.init()
            # needs to be a universal path vvv
            mixer.music.load('/Users/alexanderhaislip/Projects/Terminal_Jeopardy/Jeopardy_Theme Song.mp3')
            mixer.music.stop()
            print("Stopping...")
            return


# If the command has 'install' then it will play the jeopardy theme song until 'done' is seen...
