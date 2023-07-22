import time
import random
from selenium import webdriver
import selenium.common
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from .app_controller_interface import AppController


class BumbleController(AppController):

    web_base_url = "https://bumble.com/app"

    notifications = {
        "max_likes": ''
    }
    
    def open_web(self) -> None:
        options = webdriver.ChromeOptions()  # create options var
        
        # run this command below on cmd where chrome.exe is and than run this function (only need to be done once)
        # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # make chrome to not close
        
        self.driver = webdriver.Chrome(options)  # install required chrome
        # driver with desired options
        self.driver.get(self.web_base_url)

    def swipe_right(self):
        keep_going = True
        try:
            self.click('//*[@id="quickmatch-aria-tabpanel"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/button')
        except selenium.common.exceptions.ElementClickInterceptedException:
            notification, xpath = self.check_notifications()
            if notification:
                keep_going = self.decide(notification, xpath)
        return keep_going
            

    def check_notifications(self):
        for notification, xpath in self.notifications.items():
            try:
                self.driver.find_element(By.XPATH, xpath)
                return notification, xpath
            except:
                pass
        return None, None
    
    def click(self, xpath) -> None:
        time.sleep(random.random() + random.random() + 1)
        self.driver.find_element(By.XPATH, xpath).click()
    
    def decide(self, notification, xpath):
        if notification == "max_likes":
            self.click(xpath)
            return False
        else:
            raise Exception