import time
tupClass = ("Brian", "Marco", "Carl", "Xavier", "Eric", "Edwin", "Ian", "Demitrious", "Chris", "Ryan", "Adam", "Fabian")
print('These are all my students. This is my Math class!')
for student in tupClass:
    print(student)
    time.sleep(.25)

print("Today we are going to do basic math.")
time.sleep(.25)
print("To find a square root of a number you find it like you divdie it. For example the square root of 100 would be 100 / 10 which is....")
time.sleep(.25)
import math
time.sleep(.25)
print(math.sqrt(100))
time.sleep(.25)
print("So there you have square rooting you just divide it by whatever the square root is.")
time.sleep(.25)
N = 20
Number_list = ['10', '40', '30', '20']
print("Now lets try to figure out the mystery number (N) by using less, greater and equal signs")
time.sleep(.25)
print("This is our list: " + str(Number_list))
time.sleep(.25)
print("Now lets figure out what N is.")
time.sleep(.25)
if 10 < N:
    print("10 is less than N.")
elif 10 > N:
    print("10 is greater than N.")
else:
    print("10 = N, we found what N is.")
time.sleep(.25)
print("Now we know N is greater than 10. Lets compare the next number on the list.")
time.sleep(.25)
if 40 < N:
    print("N is less than 40.")
elif 40 > N:
    print("40 is greater than N.")
else:
    print("40 = N, we found what N is.")
time.sleep(.25)
print("We just found that 40 is greater than N. So N is greater than 10 and less than 40.")
time.sleep(.25)
print("Now lets do the next number 30.")
time.sleep(.25)
if 30 < N:
    print("30 is less than N.")
elif 30 > N:
    print("30 is greater than N.")
else:
    print("30 = N, we found what N is.")
time.sleep(.25)
print("Now we know 30 is greater than N.")
time.sleep(.25)
print("Now lets do our last number 20.")
time.sleep(.25)
if 20 < N:
    print("20 is less than N.")
elif 20 > N:
    print("20 is greater than N.")
else:
    print("20 = N. We just found our number!!")

time.sleep(.25)
print("Now lets do multiplication and division.")
print("What is N(20) * 10?")
A = N * 10
print("20 times 10 is equal to " + str(A))
print("Now lets do some division.")
A2 = N / 10
print("20 divided by 10 is equal to " + str(A2))

time.sleep(.25)
print("Now lets find out whether the temperature outside is above or below freezing.")
temp = 53
sunny = False
if temp > 32 and temp < 80:
    print("The temperature is over the freezing point which is good.")
else:
    print("It's below freezing, too coldddd.")
if not sunny:
    print("It also happens to be cloudy outside.")
else:
    print("It also happens to be sunny outside.")
print("Now let's do the same but with New York City right now it is 25")
temp2 = 26
if temp2 < 32 or temp2 > 80:
    print("Its below freezing Yikessss.")
else:
    print("Its above freezing.")

print("Now lets count to 10 class.")
counter = 1 
while counter < 11:
    print(counter)
    time.sleep(.25)
    counter = counter + 1
    time.sleep(.25)



