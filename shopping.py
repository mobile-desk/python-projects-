print("""
Welcome to your shopping list.
What would you like to do.
- add : to add to the list
- remove : to remove from the list
- clear : to clear the list
- view : view list
- quit - to close the app
""")

a = True
list = []

while a:
    b = input("What would you like to do: ").strip().lower()

    if b == "add":
        w = input("What do you want to add to the list: ").strip().lower()
        list.append(w)
    elif b == "remove":
        w = input("What do you want to remove to the list: ").strip().lower()
        if w in list:
            list.remove(w)
        else:
            print("Not found")
    elif b == "clear":
        list.clear()
    elif b == "quit":
        quit()
    elif b == "view":
        print(list)
    else: 
        print("invalid command")


