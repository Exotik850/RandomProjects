import yagmail
import time
from time import sleep
<<<<<<< HEAD
import time
=======
import concurrent.futures
import threading

>>>>>>> c7414f5cce7fcbe761309ae459d3b23ba3f15499
class SpamMail:
    def __init__(self):
        self.email = 'iamabotforme@gmail.com'
        self.password = 'ThisIsAPassword'
        self.yag = yagmail.SMTP(self.email, self.password)

    def Spam(self, count, email):
        for i in range(int(count)):
            try:
<<<<<<< HEAD
                self.yag.send(email, str(i + 1), "Hahaha I've sent you this " + str(i) + " times before!")
=======
                self.yag.send(email, str(i), "Hahaha I've sent you this " + str(i) + " times before!")
<<<<<<< HEAD
            except KeyboardInterrupt:
                print("Process Terminated")
                break
            except:
                print("Error occurred")
            else:            
                print("Email number " + str(i) + " sent.")
            sleep(0.3)
=======
>>>>>>> c65373e4f848a6903b2748f753adeeefb491e58c
            except:
                print("Error Occured")
            else:
                print(f"Email #{i + 1} sent")
            sleep(0.1)

>>>>>>> c7414f5cce7fcbe761309ae459d3b23ba3f15499
if __name__ == '__main__':
    count = input("How many emails: ")
    email = input("Email: ")
    startTime = time.perf_counter()
    sm = SpamMail()
<<<<<<< HEAD
    sm.Spam(count, email)
    print(f"Done in {round(time.time() - startTime, 2)} second(s)")
=======

    timeTaken = time.perf_counter() - startTime
    print(f"Done in {timeTaken} second(s)")
    
        
    
>>>>>>> c7414f5cce7fcbe761309ae459d3b23ba3f15499



    