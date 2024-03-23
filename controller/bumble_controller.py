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
        "max_likes": '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div/section/div/div[2]/div',
        "new_match": '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div',
    }
    
    def __init__(self, driver) -> None:
        self.driver = driver

    def open_web(self) -> None:
        self.driver.get(self.web_base_url)

    def swipe_right(self):
        keep_going = True
        try:
            self.click('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')
        except selenium.common.exceptions.NoSuchElementException:
            notification, xpath = self.check_notifications()
            if notification:
                keep_going = self.decide(notification, xpath)
        return keep_going
            
    def swipe_left(self):
        keep_going = True
        try:
            self.click('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
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
        time.sleep(random.random() + random.random() + 0.2)
        self.driver.find_element(By.XPATH, xpath).click()
    
    def decide(self, notification, xpath):
        if notification == "max_likes":
            print("new match")
            return False
        if notification == "new_match":
            self.click(xpath)
            return True
        else:
            print("unknown exception")
            time.sleep(5)
            return True
