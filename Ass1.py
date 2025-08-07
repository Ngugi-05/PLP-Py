operator = input("Enter operator(+ - * /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if operator == "+":
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
else:
    print(f"{operator} is not a valid operator")