print("""
Welcome to my calculator,
Here are a list of accepted operators:
    *,+,-,/,%,**
Do check our guide for more info
""")
a = input('What do you want to calculate? ')

try:
    u = eval(a)
    print(f"{a} = {u}")
except:
    print('An error occurred')
    exit()
