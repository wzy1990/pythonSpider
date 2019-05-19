import keyboard # pip install keyboard
from PIL import ImageGrab #pip install pillow
from aip_image import get_info_from_image

keyboard.wait(hotkey='ctrl+alt+a')
print('start')
keyboard.wait(hotkey='ctrl+f1')
print('end')

image = ImageGrab.grabclipboard()
image.save('screen.png')

print(get_info_from_image('screen.png'))