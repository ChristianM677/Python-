Name = input('Name: ')
print(" Hello " + Name + " ! We are going to figure how long you have been alive! ")
Age = int(input("How old are you? "))
print("Your are " + str(Age) + " years old .")
Months = Age * 12
#12 is the number of months in a year
Days = Age * 365
#365 is the number of days in a year
Minutes = Age * 525600
#525,600 is the number of minutes in a year
Seconds = Age * 31536000
#31,536,00 is the number of seconds in a year
print(Name + " has been alive for about: " + str(Months) + " months or " + str(Days) + " in days. In minutes you have beem alive for " + str(Minutes) + "minutes " + " and in seconds it has been " + str(Seconds) + " seconds!")