# Automatic /signcheck system for Horizon Gaming Roleplay
# Introduction
This is a simple automatic /signcheck system made in python. It works by continuously reading the last six lines from chat log text file and checking if it matches the payday string. I have to mention that I recently started coding in python and I'm a newbie, so this was my small project I had in mind to create. The packages used in this project are:
- subprocess for `checkcall`
- sys for `executable`
- os for `exists` and `makedirs`
- re for `search`
- time for `sleep`
- win32api for `mouse_event`
- win32con for `MOUSEEVENTF_MOVE`
- random for `randint`
- pyautogui for `screenshot`, `press`, `write`, and `hotkey`
- pytesseract for `image_to_string`
- cv2 for `cvtColor`, `COLOR_RGB2BGR`, and `imwrite`
- numpy for `array`
- PIL for `openimg`
- file_read_backwards for obvious reason

# Installation
Go to `main.py` and edit `chat_log_path` to your game chat log file. Example how it should look like:
```
chat_log_path = r'C:\GTA San Andreas User Files\SAMP\chatlog.txt'
```
Make sure you include \chatlog.txt not just your SAMP directory!

I haven't really tested it, but everything you should have is python3 installed, pip and `Pillow` which you can get:
```
python3 -m pip install --upgrade Pillow
```

Also make sure you instll `tesseract.exe` (https://github.com/UB-Mannheim/tesseract/wiki)
The default location for it is already set inside `main.py` → `tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`
The rest should be taken care of (not tested) as I've made it so every missing module installs itself.

# Usage
I recommend using this when you are AFK, and do not tab out, otherwise the code won't work. The script is continuously reading the last six lines from your chat log text file. If it notices that the text was payday string, it will automatically send input to open the dialog(t/signcheck). Once the dialog is opened, it will take a screenshot of your screen, save it inside `Screenshots` folder. Don't worry, there won't be more than one `Screenshot.png` and one `Screenshot.txt` files, I realised it would be a bad idea because of storage. Right before the screenshot is taken, it will move your mouse for random amount(`-1000 - 1000` on both axis). Why? Because sometimes the colors get in the way (at least I guess that's the issue), and upon reading the text from picture it fails to detect the `Check code:` string. So I decided to randomly move the mouse till it gets to the sweet spot before sending the payday code, and hitting enter.

# Video
https://user-images.githubusercontent.com/45196430/187726679-a8764c91-31e8-4239-b32e-4b92ee12e556.mov

