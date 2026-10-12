# This is the concept of strings 

# Ask for two numbers and display:
#sum, difference, product, quotient, floor quotient, remainder, power.
# n1=int(input("Enter a number 1:"))
# n2=int(input("Enter a number 2:"))

# operators=input("add/sub/mul/div/floor/power:")
# if(operators == "add"):
#     print("Addition:",n1+n2)
# elif(operators == "sub"):
#     print("Subtraction:",n1-n2)
# elif(operators == "mul"):
#     print("Multiplication:",n1*n2)
# elif(operators == "div"):
#     print("Remainder:",n1/n2)
# elif(operators == "floor"):
#     print("Floor division:",n1//n2)
# elif(operators == "power"):
#     print("Power:",n1**n2)
# else:
#     print("Invalid operators")

# Practice level-1
# Find quotient and remainder of two numbers.
# num1=int(input("Enter a number 1:"))
# num2=int(input("Enter a number 2:"))
# print("Quotient:",num1//num2)
# print("Remainder:",num1%num2)

# Check whether a number is even.
# n=int(input("Enter a number:"))
# if(n%2==0):
#     print("Even")
# else:
#     print("Odd")

# Compare two ages.
# age1=79
# age2=78
# print(age1==age2)  # This format return in boolean format like true or false

# Check whether a username exists in a list.
# username=["Jalal","Jl","Manutd"]
# print("Jalal" in username)

# Practice — Level 2
# Check whether a person is eligible based on age and another condition.
# age=int(input("Enter your age:"))
# if(age>=18):
#     print("You are eligible for license")
# else:
#     print("You are not eligible for license")

# Check whether a number is between two limits.
# number1=int(input("Enter a start:"))
# number2=int(input("Enter a end:"))
# for i in range(number1,number2):
#     print(i)

# Use += to build a running total.
football=550
bat=750
basketball=950
print("Enter a product name")
product=input("football/bat/basketball:")
if(product == "football"):
    football+=50
    print("The price of football:",football)
elif(product == "bat"):
    bat+=100
    print("The price of bat:",bat)
elif(product == "basketball"):
    basketball+=50
    print("The price of basketball:",basketball)
else:
    print("Invalid operators")


