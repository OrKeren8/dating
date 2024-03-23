from controller import WebDriver, OkcupidController, AppController, BumbleController

web_driver = WebDriver()

def get_okcupid_controller() -> AppController:
    okcupid_controller = OkcupidController(web_driver.get_driver())
    return okcupid_controller

def get_bumble_controller() -> AppController:
    bumble_controller = BumbleController(web_driver.get_driver())
    return bumble_controller

def get_web_driver():
    return web_driver.get_driver()