#create acronyms using python

word = input("Enter word: ").strip()

word = word.split()

acro = ""

for i in word:
    acro = acro+i[0]

acro = acro.upper()

print(acro)