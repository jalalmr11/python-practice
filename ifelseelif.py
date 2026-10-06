# Check number is odd or even
number=int(input("Enter a number:"))
if(number%2==0):
    print("This is even number")
else:
    print("This is odd number")

# Check positive/negative/zero.

num=int(input("Enter a number:"))
if(num>0):
    print("Positive number")
elif(num<0):
    print("Negative Number")
elif(num==0):
    print("Number is Zero")
else:
    print("Invalid number")

# Check pass/fail

mark=int(input("Enter your mark:"))
if(mark<35):
    print("you failed the subject")
else:
    print("Congrats you passed the subject")

# Compare two numbers.

cmp_num=79
if(cmp_num==79):
    print("The Number is same")
else:
    print("The number is different")

# Pratice level 2
# Find the largest of two numbers.

num1=30
num2=40
if(num1>num2):
    print("Num1 is greater")
else:
    print("Num2 is greater")

# Find the largest of three numbers.
num1=7
num2=6
num3=5
if(num1>=num2 and num1>=num3):
    print("Num1 is greater",num1)
elif(num2>=num1 and num2>=num3):
    print("Num2 is greater",num2)
else:
    print("Num3 is greater",num3)

# Grade calcluator

mark1=int(input("Enter your mark:"))
if(mark1<35):
    print("You failed the exam")
elif(mark1==35 and mark1>35):
    print("You just passed the exam")
elif(mark1>50 and mark1<=70):
    print("Average mark")
elif(mark1>70 and mark1<=85):
    print("Good mark")
elif(mark1>85 and mark1<=100):
    print("Excellent mark")

# Create a simple calculator using if/elif.

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
operation=input("add/sub/mul/div:")

if(operation == "add"):
    print(num1+num2)
elif(operation == "sub"):
    print(num1-num2)
elif(operation == "mul"):
    print(num1*num2)
elif(operation == "div"):
    print(num1/num2)
else:
    print("Invalid operations")

# Check leap year conditions.

year=int(input("Enter a year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Ask for a number and display positive, 
# negative, or zero. Then extend it to 
# identify whether a positive number is even or odd.

num=int(input("Enter a number:"))
if(num>0):
    if(num%2==0):
        print("Positive and even number")
    else:
        print("Odd numbers")

elif(num<0):
    print("Number is negative")
else:
    print("Number is equal to zero")

