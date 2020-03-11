from random import choice

sl = 4  #start length
ml = 8 #max length 
ls = '9876543210qwertyuiopasdfghjklzxcvbnm' # list
g = 0
tries = 0

file = open("file.txt",'w') #your file

for j in range(0,len(ls)**4):
    while sl <= ml:
        i = 0
        while i < sl:
            file.write(choice(ls))
            i += 1
        sl += 1
        file.write('\n')
        g += 1
    sl -= g
    g = 0
    print(tries)
    tries += 1


file.close()

