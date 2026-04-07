age = int(input("Enter your age : "))

if age > 59:
    print("Senior Citizen")
elif age >19 and age < 60:
    print("Adult")
elif age >12 and age<20:
    print("teenager")
else:
    print("Child")