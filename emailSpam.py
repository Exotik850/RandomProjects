import yagmail
from time import sleep
import concurrent.futures

class SpamMail:
    def __init__(self):
        self.email = 'iamabotforme@gmail.com'
        self.password = 'ThisIsAPassword'
        self.yag = yagmail.SMTP(self.email, self.password)

    def Spam(self, count, email):
        for i in range(int(count)):
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                    executor.map(self.yag.send(email, str(i), "Hahaha I've sent you this " + str(i) + " times before!"), email)
            except:
                print("Error occurred")
            else:            
                print("Email number " + str(i) + " sent.")
            sleep(0.1)
    
    
if __name__ == '__main__':
    count = input("How many emails: ")
    email = [input("Email: ")] * 5
    sm = SpamMail()
    sm.Spam(count, email)



    