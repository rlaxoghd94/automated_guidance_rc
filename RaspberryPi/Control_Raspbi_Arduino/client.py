import keyboard
from time import time
button_delay = 0.2

while True:
        if keyboard.is_pressed('q'):
            print('Quit!')
            break
        elif keyboard.is_pressed('a'):
            print('Left!')
            sleep(button_delay)
        elif keyboard.is_pressed('w'):
            print('Forward!')
            sleep(button_delay)
        elif keyboard.is_pressed('d'):
            print('Right!')
            sleep(button_delay)
        elif keyboard.is_pressed('s'):
            print('Stop!')
            sleep(button_delay)
        else:
            pass
