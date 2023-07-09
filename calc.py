a = int(input("Input a value here: "))
b = int(input("Input a value here: "))
c = input("Input an operator [+,-,*,/,//,%,**]: ").strip()

if c == "+":
    print(a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    print(a/b)
elif c == "//":
    print(a//b)
elif c == "%":
    print(a%b)
elif c == "**":
    print(a**b)
else:
    print("invalid input")
print("done")