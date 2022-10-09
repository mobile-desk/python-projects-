#updating pasword generator

import random
import string
from unittest import result

def password(l):
    letters = string.ascii_letters + string.digits + string.punctuation
    result = ''.join(random.choice(letters) for i in range(l))
    print(result)

length = int(input('How long do you want the password? '))

password(length)
