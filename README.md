# Description

Python 3 Selenium script to fill out Daily Self Assessment. Requires user input to select "YES" or "NO". Current configuration will prompt you to manually fill out the assessment if you choose "YES".

Uses Firefox/Geckodriver by default. Has support for Chrome/Chromedriver but headless mode is bugged.

# How To Use

Script must be started from command line. It can be run in three ways:
* Dumb Mode
* Argument Mode
* Config File Mode

Install required packages with `pip3 install -r requirements.txt`

Geckodriver or Chromedriver must be in your PATH variable. Process to do so is dependant on your Operating System:
* [Windows](https://docs.alfresco.com/4.2/tasks/fot-addpath.html)
* [Mac](https://www.architectryan.com/2012/10/02/add-to-the-path-on-mac-os-x-mountain-lion/)
* If you have linux you know this already

### Dumb Mode

Enter `python3 HealthBot.py`

Answer the prompts

### Argument Mode

Enter `python3 HealthBot.py -u username -p password -s symptoms`

Or

Enter `python3 HealthBot.py -u username -p password -s symptoms --headless`

### Config File Mode

Run `python3 setUp.py` and follow the prompts.

Config file is encrypted with RIT password and saved in "config.json" inside the script's directory.

Since its encrypted, your password is required at run time.
Symptom choice is still required at runtime as well.

Enter `python3 HealthBot.py`

Follow the prompts.
