import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
        title = "please Drink Water.....! ",
        message = "\n Whiskey is for drinking; water is for fighting over. 😀🥛",
        app_icon = "watericon.ico",
        timeout= 12
        )
        time.sleep(60*60)

        # note : if you run this program using pythonw.Drink water.py it will run even after closing the terminal in particular
        # time that has been allocated in the program 

   
