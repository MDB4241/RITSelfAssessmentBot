from selenium import webdriver
import time
import datetime
import sys

class HealthBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.base_url = "https://dailyhealth.rit.edu"


    def log(self, string):
        prefix = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S") + " | "
        print(prefix+string)

    def click_button(self, xpath):
        try:
            button = self.driver.find_element_by_xpath(xpath)
            button.click()
        except Exception:
            self.click_button(xpath)
            time.sleep(1)

    def enter_data(self,id,data):
        try:
            field = self.driver.find_element_by_id(id)
            field.send_keys(data)
        except Exception:
            self.enter_data(id,data)
            time.sleep(1)

    def element_exists(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except Exception:
            return False



    def sign_in(self):
        self.log("Attempting to sign in...")
        self.driver.get(self.base_url)

        # Enter creds
        self.enter_data("username",self.username)
        self.enter_data("password",self.password)
        self.log("Entering credentials...")

        #Sign in submission
        self.click_button("//form/button[@type='submit']")
        self.log("Submitting credentials...")

    def assess(self):
        self.log("Filling out assessment...")

        self.click_button("//a[contains(text(),'I agree')]")

        self.click_button("//div[text()='NO']")


    def confirm(self):
        """
        Confirm existence of "Cleared to Circulate" text and notify user
        """
        self.log("Confirming...")

        if self.element_exists("//div[contains(text(),'Cleared to Circulate')]"):
            self.log("Assessment Successful!")
            #Notify
        else:
            self.log("Assessment Failed!")
            #Notify

        self.driver.quit()
        sys.exit(0)


def main():
    creds = ["joeshmoe@fake.com", "blahblah"]
    if len(sys.argv)==3:
        creds = sys.argv[1:]

    bot = HealthBot(creds[0], creds[1])

    bot.driver.implicitly_wait(1)

    bot.sign_in()

    bot.assess()

    bot.confirm()


main()