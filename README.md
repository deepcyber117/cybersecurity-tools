To run the provided keylogger code on a Linux system and upload it to GitHub, follow these steps:

# Keylogger

This is a simple keylogger that logs keystrokes and sends the log to a specified email address when the ESC key is pressed.

## Prerequisites

1. Python 3.x
2. `pynput` library
3. Internet connection for sending the email

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/keylogger.git
   cd keylogger
Install the required Python packages:
bash
Copy code
pip install -r requirements.txt
Usage
Open keylogger.py in a text editor and update the email credentials:

python
Copy code
sender_email = "your-email@gmail.com"
receiver_email = "your-email@gmail.com"
password = "your-email-password"
Run the keylogger:

bash
Copy code
python keylogger.py
Press the ESC key to stop logging and send the log to the specified email address.

Security Notice
Be aware that running keyloggers can be illegal and unethical if used without consent. This code is for educational purposes only.

License
This project is licensed under the MIT License.

perl
Copy code

### requirements.txt

```txt
pynput
Steps to Run the Code on Linux
Install Python and Pip
Ensure you have Python and Pip installed on your Linux system. You can install them using the following commands:

bash
Copy code
sudo apt update
sudo apt install python3 python3-pip
Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/keylogger.git
cd keylogger
Install Dependencies
Install the required dependencies using the provided requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Update Email Credentials
Open keylogger.py in a text editor and replace the email credentials with your own:

python
Copy code
sender_email = "your-email@gmail.com"
receiver_email = "your-email@gmail.com"
password = "your-email-password"
Run the Keylogger
Run the keylogger using the following command:

bash
Copy code
python keylogger.py
The keylogger will start, and you can press the ESC key to send the log to the specified email address and exit the program.
