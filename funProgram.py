#This program will decide if you are old enough to drink alcohol

import time
print("Hello, whats your name: ")
name = input()
print(f"Hello {name}")
time.sleep(.50)
print("By typing down your age I will tell you if you are able to drink or not.")

print("So what is your Age: ")
Age = input()
if Age >= str(21):
    print("U are legally allowed to drink go party!!!")
    
elif Age < str(21):
    print("U are too young sorry")
time.sleep(.50)

def happy_birthday():
    print(f"Happy birthday to you {name} !!")
    print("U r 1 year older than yesterday!!")
answer = input("Is it your birthday?")
if answer == "Yes":
    happy_birthday()
elif answer == "No":
    print("Keep waiting")


import os