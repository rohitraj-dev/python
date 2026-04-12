# number = 5

# for i in range(1, number + 1):
#     factorial *= i
    
# print(factorial) 

number = 5
factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1
    
print(factorial)