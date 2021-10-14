Permission = "Windows"
guess = ""
guess_count = 2
guess_limit = 3
out_of_guesses = False
screen_clear = False

while guess != Permission and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Type Windows To Continue Or No To Cancel: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Application Stopped")
else:
    print("You Have Given Permission To The Application To Continue"
          " Thank You!!!")
    print("The Application Will Now Continue")

    import time

    time.sleep(2.4)
    print("Downloading Required Assets")

    import time

    time.sleep(2.4)
    print("Connecting To the databases")

    import time

    time.sleep(2.4)
    print("Succesfully connected to databases")

    import time

    time.sleep(2.4)
    print("Updating Database")

    import time

    time.sleep(2.4)
    print("Reestablishing Secure Connection To Database")

if out_of_guesses:
    screen_clear
else:

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

if out_of_guesses:
    screen_clear
else:

    import time

    time.sleep(0.1)
    print(":Updating Application")

    import time

    time.sleep(0.1)
    print("This Proccess Will Take About 1 Minute")

    import time

    time.sleep(0.1)
    print("Updating Application Modules")

    import time

    time.sleep(30.0)
    print("Application Modules Are Updated")

    import time

    time.sleep(0.1)
    print("Updating Application Files And Folders")

    import time

    time.sleep(20.0)
    print("Application File And Folders Are Updated")

    import time

    time.sleep(0.1)
    print("Upgrading Application To Premium Version ")

    import time

    time.sleep(10.0)
    print(
        "Application Is Successfully Upgraded and Updated To Version: PV1.1.3"
    )

if out_of_guesses:
    screen_clear
else:

    import itertools
    import threading
    import time
    import sys

    done = False
    '|', '/', '-', '\\'

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rScanning Your PC ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(
            '\rWe Could Ditect A Virus Which Is Currently Running On Your PC...     '
        )

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(10)
    done = True

if out_of_guesses:
    screen_clear
else:

    import time

    print("Warning!")
    time.sleep(2.4)
    print("")

if out_of_guesses:
    screen_clear
else:

    import itertools
    import threading
    import time
    import sys

    done = False
    '|', '/', '-', '\\'

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rObtaining More Infomation ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write(
            '\rThe Virus Is Severe. Please Scan Your PC With Microsoft Secuirity. The Microsoft Certified Virus Scanner     '
        )

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(10)
    done = True

if out_of_guesses:
    screen_clear
else:

    import time

    print("Application Was Unable To Locate The Virus")
    time.sleep(2.4)
    print("")
