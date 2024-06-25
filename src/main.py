from pynput.keyboard import Listener, Key, KeyCode
from pynput.mouse import Controller

mouse: Controller = Controller()
def get_position(pressed: Key | KeyCode) -> None:
    if isinstance(pressed, KeyCode) and pressed.char == 't':
        print(mouse.position)

with Listener(on_press=get_position) as listener:
    listener.join()