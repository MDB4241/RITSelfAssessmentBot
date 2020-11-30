from configData import ConfigData
from crypto import Crypto
import getpass


def main():
    username = None
    password = None

    while True:
        try:
            username = input("Enter your RIT username: ")
            break
        except Exception:
            continue

    while True:
        try:
            password = getpass.getpass("Enter your password (No text will appear in console): ")
            break
        except Exception:
            continue

    crypto = Crypto(password)


main()