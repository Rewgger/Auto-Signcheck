from imports import (
                        screenshot,                             # Will be used for taking a screenshot of the screen
                        pytesseract,                            # Will be used for reading the text from the screenshot
                        exists as file_exists,                  # Will be used for checking whether file exists or not
                        makedirs as create_folder,              # Will be used for creating a folder
                        cvtColor as convert_color,              # Will be used for converting a screenshot to another color space
                        array,                                  # Will be used for storing a screenshot into array
                        COLOR_RGB2BGR as rgb_to_bgr,            # Will be used for converting rgb to bgr color space,
                        imwrite as save_screenshot,             # Will be used for saving a screenshot
                        openimg as open_screenshot,             # Will be used for opening a screenshot
                        image_to_string,                        # Will be used for extracting text out a screenshot
                        search as regex_search,                 # Will be used for extracting payday code out text file
                        FileReadBackwards as read_backwards,    # Will be used for reading chat log backwards
                        press as keyboard_press,                # Will be used for clicking a button on our keyboard
                        write as keyboard_write,                # Will be used for writing text with our keyboard
                        sleep as wait_seconds,                  # Will be used for stopping the code for X seconds
                        hotkey as macro,                        # Will be used for using a macro, such as CTRL+V
                        mouse_event as trigger_mouse,           # Will be used for moving mouse, to prevent the corrupt screenshot text reading
                        MOUSEEVENTF_MOVE as move_mouse,         # Same as above
                        randint                                 # Random integer
                    )


# Pointing the path to tesseract.exe (NOTE: That is the default location of tesseract.exe)
# * You might have to install the setup yourself (https://github.com/UB-Mannheim/tesseract/wiki)
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Path of our screenshots folder, ensure it's created if doesn't exist before even doing anything
screenshots_path = 'Screenshots'
if not file_exists(screenshots_path):
    create_folder(screenshots_path)

chat_log_path = r'!YOUR CHAT LOG DIRECTORY, INCLUDE chatlog.txt AS WELL!'

# Let the 'incremented ID' always be 0, to save space, and the files will be replaced anyways
def get_next_increment_name() -> str:
    return f'{screenshots_path}\Screenshot_0.png'

# Takes a screenshot of the screen, stores the new screenshot inside `screenshots_path` folder
# This function returns the name of our new screenshot as well
def take_screenshot():
    screenshot_name = get_next_increment_name()

    image = screenshot()
    image = convert_color(
                            array(image),
                            rgb_to_bgr
                         )

    save_screenshot(screenshot_name, image)

    return screenshot_name

# Reads a screenshot, exports the text out, and returns it
def read_screenshot(screenshot: str) -> str:
    if not file_exists(screenshot):
        print(f'I couldn\'t open [{screenshot}], please ensure its existance.')
        return
    
    image_screenshot = open_screenshot(screenshot)

    return image_to_string(image_screenshot)

# Saves text inside screenshot text file
def save_screenshot_text(screenshot: str, text: str):
    with open(f'{screenshot}.txt', '+w', encoding = 'utf8') as screenshot_file:
        screenshot_file.write(text)
        screenshot_file.close()
        return f'{screenshot}.txt'

# Extracts the paycheck code out the screenshot text, and return it
def find_paycheck_code(screenshot: str) -> int:
    if not file_exists(screenshot):
        print('The text file for that screenshot does not exist.')
        return
    
    with open(screenshot, 'r', encoding = 'utf8') as screenshot_file:
        for line in screenshot_file:
            if 'Check code:' in line:
                return int(regex_search(r'\d+', line).group())
    
    return -1

# Checkes if the payday is ready
def is_payday_ready() -> bool:
    is_ready = 0

    with read_backwards(chat_log_path) as chat_log_file:
        index = 0

        for line in chat_log_file:
            if index >= 6:
                break

            if '/signcheck' in line:
                is_ready += 1
            elif '______________________________________' in line:
                is_ready += 1
            
            index += 1
        
    return True if is_ready >= 2 else False

# Opens the /signcheck dialog
def open_payday_dialog():
    keyboard_press('t')
    keyboard_write('/signcheck')
    keyboard_press('enter')

while True:
    if is_payday_ready(): 
        # Attempt twenty times to find the payday code, if it is unable to, something went terribly wrong
        # Will move the mouse till it gets the 'sweet spot' or 'count' reaches zero
        payday_code = -1
        count = 20

        while payday_code == -1 and count > 0:
            keyboard_press('esc')
            
            trigger_mouse(move_mouse, randint(-1000, 1000), randint(-1000, 1000), 0, 0)

            open_payday_dialog()

            wait_seconds(1)

            payday_screenshot = take_screenshot()
            screenshot_text = read_screenshot(payday_screenshot)
            text_file = save_screenshot_text(payday_screenshot, screenshot_text)
            payday_code = find_paycheck_code(text_file)
            count -= 1

        macro('ctrl', 'a')

        wait_seconds(0.5)

        keyboard_write(str(payday_code))

        keyboard_press('enter')