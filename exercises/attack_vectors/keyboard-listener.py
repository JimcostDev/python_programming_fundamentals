
"""
instalar pynput:
    pip install pynput
    
Este script imprime en consola las teclas que se presionan, hasta que se presiona la tecla 'esc'
Es un simulador de keylogger, pero no guarda las teclas presionadas en ningún archivo.
"""
from pynput.keyboard import Listener, Key

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    if key == Key.esc:
        # Stop listening on Esc press
        return False

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()