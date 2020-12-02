from configData import ConfigData
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

    #TODO: ask for headless or not

    config_data = ConfigData(username, password)

    config_data.save()



main()