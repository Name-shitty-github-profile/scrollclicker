# number of click per schroll
number = 1
# code
import pyautogui
from pynput.mouse import Listener, Controller, Button
pyautogui.FAILSAFE = True
ctrl = Controller()
button = Button.left
if number == 1:
    def on_scroll(x, y, dx, dy):
        ctrl.click(button)
else:
    def on_scroll(x, y, dx, dy):
        for i in range(number):
            ctrl.click(button)
    
mouse = Listener(on_scroll=on_scroll)
mouse.start()
mouse.join()
