def getNum(num):
    while True:
        operand = input("Num" + str(num) + ": ")
        try:
            return float (operand)
        except:
            print("Invalid number, try again.")

operand = getNum(1)
operand1 = getNum(2)
sign = input("Sign: ")


try:
    operand= float(operand)
    operand1= float(operand)
    valid = True
except:
    print("Invalid operand")

if valid:
    result = 0
    if sign == "+":
        result = operand + operand1
    elif sign == "-":
        result = operand - operand1
    elif sign == "/":
        result = operand / operand1
        if float(operand1) != 0:
            result= float(operand) / float(operand1)
        else:
            print("Division by zero.")
    elif sign == "*": 
        result = operand *  operand1

    print(result)