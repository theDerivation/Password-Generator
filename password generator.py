import random
import string

import string
import random

letters = string.ascii_uppercase + string.ascii_lowercase + string.punctuation

characters = int(input("Enter number of characters "))
password = ""

for character in range(1, characters + 1):
  password += random.choice(letters)
print(password)
