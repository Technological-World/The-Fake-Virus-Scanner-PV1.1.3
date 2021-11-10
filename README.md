# The-Fake-Virus-Scanner-PV1.1.3
Created By Technological World. All Rights Reserved ® 
mostly used coding to control time of the messege appears:

    import itertools
    import threading
    import time
    import sys

    done = False

    #here is the animation
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rChecking For Updates ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rUpdate Available: ')

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(10)
    done = True
