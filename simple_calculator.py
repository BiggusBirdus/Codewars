"""You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.
if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned."""

def main():
    x = int(input("x: "))
    y = int(input("y: "))
    op = input("op: ")

    result = calculator(x, y, op)
    print(result)

def calculator(x, y, op):
    # check if x and y are not integers
    if not isinstance(x, int) or not isinstance(y, int):
        return "unknown value"
    
    # perform the operations
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "/":
        return x / y
    if op == "*":
        return x * y

    # return unknown value if operator is wrong
    return "unknown value"

main()
