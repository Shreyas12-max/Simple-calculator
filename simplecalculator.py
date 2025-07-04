# Simple calculator
# Created by Shreyas
# Date : 4th July 2025

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

print("choose operation")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

Choice = input("Enter operation symbol (+ , - , * , / ): ")

if Choice == "+":
    result = num1 + num2
    print("Result : ",result)

elif Choice == "-":
    result = num1 - num2
    print("Result :",result)

elif Choice == "*":
    result = num1 * num2
    print("Result :",result)

elif Choice == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result :",result)
    else:
        print("Error, cannot divide by zero")

else:
    print("Invalid operation.... Please choose among + , - , * , / ")
    
