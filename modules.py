import random
import math

### TASK ###
# Use ceil and float from math to make a round function

def round_task():
    choice = input("Input a number to check: ")
    checker = float(choice) % 1
    if checker >= 0.5:
        return print(math.ceil(float(choice)))
    else:
        return print(math.floor(float(choice)))

round_task()