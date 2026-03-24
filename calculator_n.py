import math
def user():
    a = float(input("Enter number"))
    return a
try:
    num_1 = float(input("Enter a number"))

    while True:
        op = input("Enter operator[+,-,*,/,pow,root or q(to exit)]").strip().lower()
        if op == "+":
            n = user()
            num_1 += n
            print(num_1)
        elif op == '-':
            n = user()
            num_1 -= n
            print(num_1)
        elif op == "*":
            n = user()
            num_1 *= n
            print(num_1)
        elif op == "/":
            n = user()
            if n == 0:
                print("Division by 0 not allowed")
            else:
                num_1 /= n
                print(num_1)
        elif op == "pow":
            exp = int(input("Enter power to be raised"))
            num_1 = math.pow(num_1, exp)
            print(num_1)
        elif op == "root":
            rt = int(input("Enter the value of n(for nth root)"))
            if rt == 0:
                print("Can't root for 0")
            else:
                num_1= math.pow(num_1,(1/rt))
                print(num_1)
        elif op == "q":
            print("Thanks for using me!!☺️, Goodbye")
            break
        else:
            print("Enter Valid Option")

except ValueError:
    print('Enter Valid Value')