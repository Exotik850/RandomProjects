import yagmail
import time
from time import sleep
import time
class SpamMail:
    def __init__(self):
        self.email = 'iamabotforme@gmail.com'
        self.password = 'ThisIsAPassword'
        self.yag = yagmail.SMTP(self.email, self.password)

    def Spam(self, count, email):
        for i in range(int(count)):
            try:
                self.yag.send(email, str(i), "Hahaha I've sent you this " + str(i) + " times before!")
            except KeyboardInterrupt:
                print("Process Terminated")
                break
            except:
                print("Error occurred")
            else:            
                print("Email number " + str(i) + " sent.")
            sleep(0.3)

if __name__ == '__main__':
    count = input("How many emails: ")
    email = input("Email: ")
    startTime = time.perf_counter()
    sm = SpamMail()
    sm.Spam(count, email)
    timeTaken = time.perf_counter() - startTime
    print(f"Done in {timeTaken} second(s)")
    




    