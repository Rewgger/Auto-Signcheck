'''
    **  Import modules which will take care of non installed modules automatically.
'''
from subprocess import check_call
from sys import executable
from os.path import exists
from os import makedirs
from re import search
from time import sleep
from win32api import mouse_event
from win32con import MOUSEEVENTF_MOVE
from random import randint

'''
    **  Define function which handles installation of specified modules.
'''
def install_module(package: str):
    check_call([executable, '-m', 'pip', 'install', package])

"""
    **  Try importing `pyautogui` module which will take care of our taking a screenshot of the screen.
    **  If the module couldn't be imported, automatically install it and import.
"""
try:
    from pyautogui import screenshot, press, write, hotkey
except ImportError:
    install_module('pyautogui')
finally:
    from pyautogui import screenshot, press, write, hotkey

"""
    **  Try importing `pytesseract` module which will take care of reading the text from a screenshot.
    **  If the module couldn't be imported, automatically install it and import.
"""
try:
    import pytesseract
    from pytesseract.pytesseract import image_to_string
except ImportError:
    install_module('pytesseract')
finally:
    import pytesseract
    from pytesseract.pytesseract import image_to_string

"""
    **  Try importing `cv2` module which will take care of converting picture from one color space to another.
    **  If the module couldn't be imported, automatically install it and import.
"""
try:
    from cv2 import cvtColor, COLOR_RGB2BGR, imwrite
except ImportError:
    install_module('opencv-python')
finally:
    from cv2 import cvtColor, COLOR_RGB2BGR, imwrite

"""
    **  Try importing `numpy` module which will take care of arrays.
    **  If the module couldn't be imported, automatically install it and import.
"""
try:
    from numpy import array
except ImportError:
    install_module('numpy')
finally:
    from numpy import array

# Run this if you get error:
# python3 -m pip install --upgrade Pillow
from PIL.Image import open as openimg

"""
    **  Try importing `file_read_backwards` module which will take care of reading files backwards.
    **  If the module couldn't be imported, automatically install it and import.
"""
try:
    from file_read_backwards import FileReadBackwards
except ImportError:
    install_module('file_read_backwards')
finally:
    from file_read_backwards import FileReadBackwards