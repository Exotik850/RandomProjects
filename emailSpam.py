import yagmail

class SpamMail():
    def __init__(self):
        self.email = 'iamabotforme@gmail.com'
        self.password = 'ThisIsAPassword'
        self.yag = yagmail.SMTP(self.email, self.password)
    def Spam(self, count, email):
        for i in range(count):
            self.yag.send(email, str(i), "Hahaha I've sent you this " + str((i-1)) + " times before!")
            print("Email number " + str(i) + " sent.")

if __name__ == '__main__':
    SpamMail.__init__(SpamMail)
    SpamMail.Spam(SpamMail, 15, 'samshiberou@gmail.com' )



    