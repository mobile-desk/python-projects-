#email slicer

email = input("Input email: ").strip()

email = email.split('@')

print(f"Your user name, {email[0]} is registered under {email[1]} domain")
