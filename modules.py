import random
import math

### TASK ###
# Use ceil and float from math to make a round function

def round_task(number):
    checker = number % 1
    if checker >= 0.5:
        return math.ceil(number)
    else:
        return math.floor(number)

print(round_task(56))
print(math.pi)
