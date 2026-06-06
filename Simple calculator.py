num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
op = input("enter operation(+,-,*,/):")

if op == "+":
    print("Result=",num1+num2)
elif op =="-":
    print("Result=",num1-num2)
elif op =="*":
    print("Result=",num1*num2)
elif op =="/":
    print("Result=",num1/num2)
else:
    print("invalid operation")