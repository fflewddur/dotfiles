import re
import logging

logging.debug("mapkeys running")

active_class = window.get_active_class()
if re.match('.*(Emacs|Gvim)', active_class):
    original = store.get_global_value('hotkey')
    keyboard.send_keys(original)
elif re.match('.*(Gnome-terminal)', active_class):
    original = store.get_global_value('hotkey')
    mapped_modifiers = re.sub(r'<super>', r'<ctrl>', original)
    logging.debug("mapped_modifiers: " + str(mapped_modifiers))
    
    # Support global navigation shortcuts
    if mapped_modifiers == "<ctrl>+<shift>+]":
        mapped_modifiers = "<ctrl>+<page_down>"
    elif mapped_modifiers == "<ctrl>+<shift>+[":
        mapped_modifiers = "<ctrl>+<page_up>"
    
    keyboard.send_keys(mapped_modifiers)
else:
    mapped_keys = engine.get_return_value()
    keyboard.send_keys(mapped_keys)
