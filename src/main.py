from pynput.keyboard import Listener, Key, KeyCode
from pynput.mouse import Controller
from typing import Callable

mouse: Controller = Controller()
def getter(toggle: Key | KeyCode) -> Callable[[Key | KeyCode], None]:
    def wrapper(pressed: Key | KeyCode) -> None:
        if pressed == toggle:
            print(mouse.position)
    return wrapper

with Listener(on_press=getter(toggle=KeyCode(char='t'))) as listener:
    listener.join()