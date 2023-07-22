from controller import *

def get_okcupid_controller() -> AppController:
    okcupid_controller = OkcupidController()
    return okcupid_controller

def get_bumble_controller() -> AppController:
    bumble_controller = BumbleController()
    return bumble_controller