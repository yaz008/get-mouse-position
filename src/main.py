from pynput.keyboard import Listener, Key, KeyCode
from pynput.mouse import Controller
from typing import Callable

mouse: Controller = Controller()
def getter(toggle: Key | KeyCode,
           exit_key: Key | KeyCode = Key.esc
           ) -> Callable[[Key | KeyCode], None]:
    def wrapper(pressed_key: Key | KeyCode) -> None:
        if pressed_key == toggle:
            print(mouse.position)
        if pressed_key == exit_key:
            exit()
    return wrapper

with Listener(on_press=getter(toggle=KeyCode(char='t'))) as listener:
    listener.join()