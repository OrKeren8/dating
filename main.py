import time
import random

import deps


def main() -> None:
    keep_going = True

    controller = deps.get_okcupid_controller()
    controller.open_web()
    time.sleep(5)
    while True:
        while keep_going:
            keep_going = controller.swipe_right()
        print("finished likes for today") 
        time.sleep(random.randrange(33000, 36000)) # wait 9 to 10 hours
    
    # controller = deps.get_bumble_controller()
    # controller.open_web()
    # time.sleep(5)
    # while keep_going:
    #     keep_going = controller.swipe_right()
    
if __name__ == "__main__":
    main()
