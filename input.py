"""
Defines methods to handle user input
"""
import getpass
import sys, datetime, getopt
from crypto import Crypto


def processArguments(args):
    """
	Process and assign arguments to variables
		:param args:	sys.argv
		:return:		Dictionary of options specified or dumbmode() to interactively determine options
	"""
    # Initialize option variables
    dumbmode = False
    headless = False
    symptoms = None
    username = None
    password = None
    run_values = {}

    # If no options given, return dumbmode()
    if len(args) == 1:
        dumbmode = True

    # Process options
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hu:p:s:', ['help','headless','symptoms'])
    except getopt.GetoptError:
        print('\nMinimum Input:')
        print('\"HealthBot.py -u <username> -p <password> -s <symptoms>\"')
        print(" or")
        print("\n\"HealthBot.py -h for more options\"\n")
        sys.exit(2)

    # Iterate through and assign options to variables
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print('\n\"HealthBot.py -u <username> -p <password> -s <yes/no>\"')
            print('\t--headless to run without visible browser')
            print('\n\"HealthBot.py\" for interactive mode')
            print('\n')
            sys.exit(1)
        elif opt == '-u':
            username = arg
        elif opt == '-p':
            password = arg
        elif opt == '-s':
            symptoms = arg
        elif opt == '--headless':
            headless = True


    # Move options into dictionary
    run_values['username'] = username
    run_values['password'] = password
    run_values['headless'] = headless

    if symptoms == 'Y':
        run_values['symptoms'] = True
    elif symptoms == 'N':
        run_values['symptoms'] = False

    # Return dictionary or dumbmode()
    if username is not None and password is not None and symptoms is not None:
        return run_values
    elif dumbmode:
        return dumbMode(run_values)
    else:
        print("You fucked up something. Try 'HealthBot.py -h' for help")
        sys.exit(1)


def dumbMode(run_values):
    """
	Interactive way to populate input options.
		:return: run_values with additional options input by user
	"""
    while True:
        try:
            run_values['username'] = input("Enter your RIT username: ")
            break
        except Exception:
            continue

    while True:
        try:
            run_values['password'] = getpass.getpass("Enter your password (No text will appear in console): ")
            break
        except Exception:
            continue

    while True:
        try:
            symptoms = input("Are you feeling any symptoms?[Y/N]: ")
            if symptoms == 'Y':
                run_values['symptoms'] = True
            elif symptoms == 'N':
                run_values['symptoms'] = False
            break
        except Exception:
            continue

    while True:
        response = input('Would you like to run headless?[Y/N]: ')
        if response.upper() == "Y":
            run_values["headless"]=True
            return run_values
        elif response.upper() == "N":
            run_values["headless"] = False
            return run_values


def configMode():
    run_values = {}

    with open('config.json', 'rb') as config:
        enc_bytes = config.read()
    password = getpass.getpass("Enter your password (No text will appear in console): ")
    crypto = Crypto(password)
    plaintext = crypto.decrypt(enc_bytes)

    #Populate run_values
    #run_values['username'] = plaintext['username']
    #run_values['password'] = plaintext['password']

    run_values['symptoms'] = input("Are you feeling any symptoms?[Y/N]: ")


    return run_values