#!/usr/bin/python3
import random
number = random.randint(-10, 10)
text = f"{number}"
if number == 0:
    text += " is zero"
else:
    text += " is positive" if number > 0 else " is negative"
print(text)
