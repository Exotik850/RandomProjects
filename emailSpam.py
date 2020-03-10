import yagmail
import time
from time import sleep
import concurrent.futures
import threading

class SpamMail:
    def __init__(self):
        self.email = 'iamabotforme@gmail.com'
        self.password = 'ThisIsAPassword'
        self.yag = yagmail.SMTP(self.email, self.password)

    def Spam(self, count, email):
        for i in range(int(count)):
            try:
                self.yag.send(email, str(i), "Hahaha I've sent you this " + str(i) + " times before!")
            except:
                print("Error Occured")
            else:
                print(f"Email #{i + 1} sent")
            sleep(0.1)

if __name__ == '__main__':
    count = input("How many emails: ")
    email = input("Email: ")
    startTime = time.time()
    sm = SpamMail()

    timeTaken = time.time() - startTime
    print(f"Done in {timeTaken} second(s)")
    
        
    



    