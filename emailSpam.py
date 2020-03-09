import yagmail
from time import sleep

class SpamMail:
    def __init__(self):
        self.email = 'iamabotforme@gmail.com'
        self.password = 'ThisIsAPassword'
        self.yag = yagmail.SMTP(self.email, self.password)
    def Spam(self, count, email):
        for i in range(count):
            try:
                self.yag.send(email, str(i), "Hahaha I've sent you this " + str((i-1)) + " times before!")
            except:
                print("Error occurred")
            else:            
                print("Email number " + str(i) + " sent.")
            sleep(1)

if __name__ == '__main__':
    SpamMail.__init__()
    SpamMail.Spam(150, 'brindha.kottu@gmail.com' )



    