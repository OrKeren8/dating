from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()  # create options var
        # run this command below on cmd where chrome.exe is and than run this function (only need to be done once)
        '''
        cd C:\Program Files (x86)\Google\Chrome\Application
        chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
        '''
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:9222")  # make chrome to not close
        self.driver = webdriver.Chrome(options)  # install required chrome

    def get_driver(self):
        return self.driver
