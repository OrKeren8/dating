import time
import random
import selenium.common
from selenium.webdriver.common.by import By
import urllib.request

from .app_controller_interface import AppController


class OkcupidController(AppController):

    web_base_url = "https://www.okcupid.com/login"

    notifications = {
        "max_likes": '//*[@id="OkModalContent-main"]/div[1]/button',
        "new_match": '//*[@id="BaseModal"]/div/button',
        "super_like": '//*[@id="BaseModal"]/button[2]'
    }
    
    def __init__(self, driver) -> None:
        self.driver = driver

    def open_web(self) -> None:
        self.driver.get(self.web_base_url)

    def swipe_right(self):
        keep_going = True
        try:
            self.click('//*[@id="quickmatch-aria-tabpanel"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/button')
        except selenium.common.exceptions.WebDriverException:
            notification, xpath = self.check_notifications()
            keep_going = self.decide(notification, xpath)
        return keep_going
            
    def swipe_left(self):
        keep_going = True
        try:
            self.click('//*[@id="quickmatch-aria-tabpanel"]/div/div/div[1]/div[1]/div[2]/div[1]/div/div[1]/button')
        except selenium.common.exceptions.ElementClickInterceptedException:
            notification, xpath = self.check_notifications()
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
            self.click(xpath)
            return False
        if notification == "new_match":
            print("new match")
            self.click(xpath)
            return True
        if notification == "super_like":
            self.click(xpath)
            return True
        else:
            print("unknown exception")
            time.sleep(5)
            return True
        
    def get_unknown_likes(self):
        self.driver.get("https://www.okcupid.com/who-likes-you")
        time.sleep(5)
        for i in range(1, 9):
            element = self.driver.find_element(By.XPATH, f'//*[@id="userRows-app"]/div/div[2]/div/a/div/div[2]/div[{i}]/div[1]/div')
            element = element.get_attribute("style")[23: len(element.get_attribute("style")) - 3]
            print(element)
            print(help(urllib.request.urlretrieve))
            urllib.request.urlretrieve(element, f"./controller/unknown_likes/{random.randrange(1, 10000)}.jpg")
