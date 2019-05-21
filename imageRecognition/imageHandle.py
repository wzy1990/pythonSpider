import keyboard # pip install keyboard
from PIL import ImageGrab #pip install pillow
from imageRecognition.aip_image import get_info_from_image

keyboard.wait(hotkey='ctrl+alt+a') # 等待截图，Ctrl + alt + a 是QQ的截图快捷键
print('start')
keyboard.wait(hotkey='ctrl+f1')
print('end')


image = ImageGrab.grabclipboard()
if image:
    image.save('screen.png')
    print(get_info_from_image('screen.png'))
else:
    print('请截图哦')