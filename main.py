import time
import random

import deps


def main() -> None:

    while True:
        
        keep_going = True
        controller = deps.get_okcupid_controller()
        controller.open_web()
        time.sleep(5)
        while keep_going:
            if random.randrange(0, 3,1) > 0:
                keep_going = controller.swipe_right()
            else:
                keep_going = controller.swipe_left()
        print("finished okcupid likes for today") 
        
        keep_going = True
        controller = deps.get_bumble_controller()
        controller.open_web()
        time.sleep(5)
        while keep_going:
            # if random.randrange(0, 3,1) > 0:
            keep_going = controller.swipe_right()
            # else:
            #     keep_going = controller.swipe_left()
        print("finished okcupid likes for today")

        idle_time = random.randrange(33000, 36000) # wait 9 to 10 hours
        print(f"idle for {idle_time/3600} hours")
        time.sleep(idle_time)
    
    
if __name__ == "__main__":
    main()
