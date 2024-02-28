# #!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == "admin" and password == "12345" :
        return "Access granted"
    else:
        return "Access denied"
admin_login("sudo", "12345")
# "Access denied"
admin_login("admin", "12345")
# "Access granted"
admin_login("ADMIN", "12345")
# "Access granted"

def hows_the_weather(temperature):
    # your code here
    if(temperature<40):
        return "It's brisk out there!"
    elif(temperature>=40 and  temperature<=65):
        return "It's a little chilly out there!"
    elif(temperature>85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

hows_the_weather(33)
# "Brisk!"
hows_the_weather(99)
# "Too dang hot"
hows_the_weather(75)
# "Perfect!"
    


def fizzbuzz(num):
    # your code here
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3) == 0 :
        return "Fizz"
    elif (num % 5)==0:
        return "Buzz"
    else:
        return num
    
fizzbuzz(1)
# 1
fizzbuzz(2)
# 2
fizzbuzz(3)
# Fizz
fizzbuzz(4)
# 4
fizzbuzz(5)
# Buzz
fizzbuzz(15)
# FizzBuzz

def calculator(operation, num1, num2):
    # your code here
    if(operation=="+") :
        return num1 + num2
    elif(operation=="-") :
        return num1 - num2
    elif(operation=="/") :  
        return num1 / num2
    elif(operation=="*") :
        return num1 * num2
    else:
        print("Invalid operation!")
        return None
    
calculator("+", 1, 1)
# 2
calculator("-", 3, 1)
# 2
calculator("*", 3, 2)
# 6
calculator("/", 4, 2)
# 2
calculator("nope", 4, 2)
# "Invalid operation!"
# None
   
