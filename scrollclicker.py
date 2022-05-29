# number of click per schroll
number = 1
# code
import pyautogui
from pynput.mouse import Listener, Controller, Button
pyautogui.FAILSAFE = True
mousee = Controller()
button = Button.left
def on_scroll(x, y, dx, dy):
    for i in range(number):mousee.click(button)
    
mouse = Listener(on_scroll=on_scroll)
mouse.start()
mouse.join()
