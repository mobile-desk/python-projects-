#check data type for all elements in a list

a = [1,"pease", 4, "dog"]

for i in a:
    if isinstance(i, int):
        print(f"{i} is an integer")
    elif isinstance(i, str):
        print(f"{i} is a string")
    else:
        pass
