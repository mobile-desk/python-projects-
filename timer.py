import time

import datetime

 

def countdown(h, m, s):

   

    total_sec = h * 3600 + m * 60 + s

   

    while total_sec > 0:

        timer = datetime.timedelta(seconds = total_sec)

       

        print(timer, end="\r")

       

        

        time.sleep(1)

       

        total_sec -= 1

       

    

    print("Timer is completed!!!!!")

   

h = input("Enter the time in hours: ")

m = input("Enter the time in minutes: ")

s = input("Enter the time in seconds: ")

 

countdown(int(h), int(m), int(s))       

