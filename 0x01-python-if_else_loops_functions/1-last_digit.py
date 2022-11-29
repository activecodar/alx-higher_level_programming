#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1]) if number > 0 else 0 - int(str(number)[-1])
text = f"Last digit of {number} is {last_digit} and is "
if last_digit == 0:
    text += "0"
elif last_digit < 6 and last_digit != 0:
    text += "less than 6 and not 0"
elif last_digit > 5:
    text += "greater than 5"
print(text)
