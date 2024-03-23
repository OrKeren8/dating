from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
from PIL import Image
import random


options = webdriver.ChromeOptions()  # create options var

options.add_experimental_option("debuggerAddress", f"127.0.0.1:9222")  # make chrome to not close
driver = webdriver.Chrome(options)  # install required chrome

for i in range(1, 9):
    element = driver.find_element(By.XPATH, f'//*[@id="userRows-app"]/div/div[2]/div/a/div/div[2]/div[{i}]/div[1]/div')
    element = element.get_attribute("style")[23: len(element.get_attribute("style")) - 3]
    print(element)

    urllib.request.urlretrieve(element, f"{random.randrange(1, 10000)}.jpg")
    # img = Image.open(str(i + 9))
    # img.show()